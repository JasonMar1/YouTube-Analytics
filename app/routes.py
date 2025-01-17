from app import app, db
from flask import render_template, redirect, url_for, flash, session, request
from app.models import User, DeviceType, Day, Gender, Month, SharingService, UploaderType, Video
from app.forms import RegisterForm, LoginForm, ChangePasswordForm
from flask_login import login_user, logout_user, login_required, current_user
from YouTube_API_Request import auth
from YouTube_API_Request.auth import json_to_credentials, credentials_to_json
from YouTube_API_Request.request_main import request_data_for_user  # Import the function
from werkzeug.security import generate_password_hash


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/analytics/<table_name>', methods=['GET'])
@login_required
def analytics_table_page(table_name):
    tables_data = {}
    selected_columns = request.args.getlist('columns')  # Get selected columns from the form

    # Ensure the table name is valid
    model_class = {
        'deviceType': DeviceType,
        'day': Day,
        'gender': Gender,
        'month': Month,
        'sharingService': SharingService,
        'uploaderType': UploaderType,
        'video': Video
    }.get(table_name)

    if model_class is None:
        flash(f'Table {table_name} does not exist in the database.', 'danger')
        return redirect(url_for('home_page'))

    try:
        # Query for data specific to the logged-in user
        items = db.session.query(model_class).filter_by(user_id=current_user.id).all()

        # Process data to remove 'id' and 'user_id' columns
        processed_rows = []
        for item in items:
            row = {column.name: getattr(item, column.name) for column in model_class.__table__.columns if
                   column.name not in ['id', 'user_id']}
            processed_rows.append(row)

        # Store the rows and column names
        all_columns = [column.name for column in model_class.__table__.columns if column.name not in ['id', 'user_id']]
        tables_data[table_name] = {
            "rows": processed_rows,
            "columns": all_columns
        }
    except Exception as e:
        flash(f'Error retrieving data: {str(e)}', 'danger')
        return redirect(url_for('home_page'))

    return render_template('analytics_page.html', tables_data=tables_data, selected_columns=selected_columns)

    # tables_data = {}
    # with app.app_context():
    #     db.reflect()  # Reflect all binds
    #     if table_name in db.Model.metadata.tables:
    #         table_obj = db.Model.metadata.tables[table_name]
    #         # Reflect table and query all rows
    #         items = db.session.query(table_obj).all()
    #         # Store the rows and column names
    #         tables_data[table_name] = {
    #             "rows": items,
    #             "columns": table_obj.columns.keys()
    #         }
    #     else:
    #         flash(f'Table {table_name} does not exist in the database.', 'danger')
    #         return redirect(url_for('home_page'))
    # return render_template('analytics_page.html', tables_data=tables_data, getattr=getattr)


@app.route('/oauth2callback')
def oauth2callback():
    flow = auth.Flow.from_client_secrets_file(
        auth.CLIENT_SECRETS_FILE,
        scopes=auth.SCOPES,
        state=session['state'],
        # redirect_uri=url_for('oauth2callback', _external=True, _scheme='https')
        redirect_uri='https://youtube-analytics-dashboard-2ac54861e0a3.herokuapp.com/oauth2callback'
    )
    print(url_for('oauth2callback', _external=True))

    flow.fetch_token(authorization_response=request.url)

    credentials = flow.credentials

    print(credentials)
    if not credentials.refresh_token:
        flash('Refresh token not found. Please re-authenticate.', 'danger')
        return redirect(url_for('login_page'))

    session['credentials'] = credentials_to_json(credentials)

    # Create or update user with Google credentials
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            user.google_credentials = session['credentials']
            db.session.commit()
            return redirect(url_for('home_page'))
    else:
        # Handle error
        flash('User not found.', 'danger')
        return redirect(url_for('register_page'))


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user_to_create = User(
                username=form.username.data,
                email_address=form.email_address.data,
                password_hash=generate_password_hash(form.password1.data)
            )
            try:
                db.session.add(user_to_create)
                db.session.commit()
                login_user(user_to_create)
                session['user_id'] = user_to_create.id
                return redirect(url_for('home_page'))
            except Exception as e:
                db.session.rollback()
                print(f"Error during commit: {str(e)}")  # Print error for debugging
                flash(f'Error: {str(e)}', 'danger')
        else:
            # Custom handling for email and password errors
            if 'email_address' in form.errors:
                for error in form.errors['email_address']:
                    if "@" not in form.email_address.data:
                        flash("The email address is missing an '@' symbol. Please enter a valid email.", 'danger')
                    else:
                        flash(f"Error in Email Address: {error}", 'danger')

            if 'password2' in form.errors:
                flash("Passwords do not match. Please make sure both password fields are identical.", 'danger')
            else:
                # Flash any other form validation errors
                for field, errors in form.errors.items():
                    if field != 'email_address' and field != 'password2':  # Skip email and password handled above
                        for error in errors:
                            flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')

    return render_template('register.html', form=form)


@app.route('/google_signup')
def google_signup():
    if 'user_id' not in session:
        flash('Please register first.', 'danger')
        return redirect(url_for('register_page'))
    return auth.start_oauth_flow()


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        print(f'Username from form: {form.username.data}')
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            print(f'User found: {user.username}')
        else:
            print('User not found.')

        if user and user.check_password_correction(attempted_password=form.password.data):
            login_user(user)
            session['user_id'] = user.id  # Ensure user_id is stored in session
            flash(f'Logged in successfully as {user.username}', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    session.pop('user_id', None)  # Remove user_id from session on logout
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))


@app.route('/profile')
@login_required
def profile_page():
    return render_template('profile.html')


@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()

    # Handle POST request (form submission)
    if request.method == 'POST':
        if form.validate():  # Validate form inputs first
            # Check if the current password is correct
            if not current_user.check_password_correction(attempted_password=form.current_password.data):
                flash('Current password is incorrect. Please try again.', 'danger')
                return redirect(url_for('change_password'))

            # Check if the new password and confirmation match
            if form.new_password.data != form.confirm_new_password.data:
                flash('New password and confirmation do not match. Please try again.', 'danger')
                return redirect(url_for('change_password'))

            # Update the password
            current_user.password = form.new_password.data  # Use the setter to hash the password
            db.session.commit()
            flash('Your password has been updated!', 'success')
            return redirect(url_for('profile_page'))
        else:
            # Handle form validation errors
            flash('Please correct the errors in the form and try again.', 'danger')
            return render_template('change_password.html', form=form)

    # Handle GET request (form display)
    elif request.method == 'GET':
        return render_template('change_password.html', form=form)


@app.route('/google_auth_status')
@login_required
def google_auth_status_page():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        google_credentials = user.google_credentials
        return render_template('google_auth_status.html', google_credentials=google_credentials)
    else:
        flash('User session not found.', 'danger')
        return redirect(url_for('login_page'))


@app.route('/donate')
@login_required
def donate_page():
    return render_template('donate.html')


@app.route('/request_data', methods=['POST'])
@login_required
def request_data():
    # Fetch the user ID from the session
    user_id = session.get('user_id')
    if not user_id:
        flash('User session not found.', 'danger')
        return redirect(url_for('login_page'))

    # Get start and end dates from the form
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    if not start_date or not end_date:
        flash('Please provide both start and end dates.', 'danger')
        return redirect(url_for('request_page'))

    try:
        # Execute the request_data_for_user function with user-provided dates
        request_data_for_user(start=start_date, end=end_date)
    except Exception as e:
        flash(f'Error requesting data: {str(e)}', 'danger')

    return redirect(url_for('home_page'))


@app.route('/request')
@login_required
def request_page():
    return render_template('request.html')


if __name__ == '__main__':
    app.run(debug=True)
