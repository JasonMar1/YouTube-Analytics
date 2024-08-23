# request_main.py
from flask import session, flash, redirect, url_for
from YouTube_API_Request.auth import get_authenticated_service
from YouTube_API_Request.data_processor import save_to_db
from YouTube_API_Request.api_requests import request
from app import app, db
from sqlalchemy.exc import SQLAlchemyError

def request_data_for_user():
    # Ensure the user is logged in by checking the session
    user_id = session.get('user_id')
    if not user_id:
        flash('User session not found. Please log in.', 'danger')
        return redirect(url_for('login_page'))

    try:
        # Get authenticated service using the user's credentials
        authenticated_service = get_authenticated_service(user_id)

        start = '2023-01-01'
        end = '2024-01-01'

        # Make the API request and process the data
        data = request(authenticated_service, start, end)

        # Iterate over the data and save each dataset to the database
        for dataset in data:
            table_name = dataset['columnHeaders'][0]['name']

            # Debugging prints for verification
            print("-------------------------")
            print(f"Table Name: {table_name}")
            print(f"Dataset: {dataset}")
            print(f"User ID: {user_id}")

            # Save the data to the database using save_to_db
            save_to_db(dataset, db, table_name, user_id)

        flash("Data has been saved to the database.", 'success')

    except SQLAlchemyError as e:
        # Handle SQLAlchemy-specific errors
        db.session.rollback()
        flash(f"A database error occurred: {str(e)}", 'danger')
        app.logger.error(f"Database error: {str(e)}")

    except Exception as e:
        # Handle any other exceptions
        flash(f"An error occurred while requesting data: {str(e)}", 'danger')
        app.logger.error(f"General error: {str(e)}")

    finally:
        # Ensure the session is always committed or rolled back
        db.session.remove()

    return redirect(url_for('home_page'))
