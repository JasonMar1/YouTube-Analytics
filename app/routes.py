from app import app
from flask import render_template, redirect, url_for, flash
from app.models import User
from app.forms import RegisterForm, LoginForm
from app import db
from flask_login import login_user, logout_user, login_required


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/analytics/<table_name>')
@login_required
def analytics_table_page(table_name):
    tables_data = {}
    with app.app_context():
        db.reflect()  # Reflect all binds
        if table_name in db.Model.metadata.tables:
            table_obj = db.Model.metadata.tables[table_name]
            # Reflect table and query all rows
            items = db.session.query(table_obj).all()
            # Store the rows and column names
            tables_data[table_name] = {
                "rows": items,
                "columns": table_obj.columns.keys()
            }
        else:
            flash(f'Table {table_name} does not exist in the database.', 'danger')
            return redirect(url_for('home_page'))
    return render_template('analytics_page.html', tables_data=tables_data, getattr=getattr)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():

        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        try:
            db.session.add(user_to_create)
            db.session.commit()
            return redirect(url_for('home_page'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    else:
        flash('There were errors in the form. Please correct them and try again.', 'danger')
    return render_template('register.html', form=form)


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
            flash(f'Logged in successfully as {user.username}', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))


if __name__ == '__main__':
    app.run(debug=True)
