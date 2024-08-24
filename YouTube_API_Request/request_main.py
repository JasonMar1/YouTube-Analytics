from flask import session, flash, redirect, url_for
from YouTube_API_Request.auth import get_authenticated_service, json_to_credentials, credentials_to_json
from YouTube_API_Request.data_processor import save_to_db
from YouTube_API_Request.api_requests import request
from app import app, db
from sqlalchemy.exc import SQLAlchemyError
import logging
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from app.models import load_user
import json


def request_data_for_user(start, end):
    user_id = session.get('user_id')
    if not user_id:
        flash('User session not found. Please log in.', 'danger')
        return redirect(url_for('login_page'))

    try:
        user = load_user(user_id).query.get(user_id)
        if not user or not user.google_credentials:
            flash('No credentials found. Please re-authenticate.', 'danger')
            return redirect(url_for('google_signup'))

        credentials = json_to_credentials(user.google_credentials)

        if credentials.expired and credentials.refresh_token:
            try:
                credentials.refresh(Request())
                user.google_credentials = json.dumps(credentials_to_json(credentials))
                db.session.commit()
            except Exception as e:
                flash(f"Error refreshing credentials: {str(e)}", 'danger')
                app.logger.error(f"Error refreshing credentials: {str(e)}")
                return redirect(url_for('google_signup'))
        elif credentials.expired:
            flash('The credentials have expired and cannot be refreshed. Please re-authenticate.', 'danger')
            return redirect(url_for('google_signup'))

        authenticated_service = get_authenticated_service(user_id)

        # Make the API request and process the data with the selected date range
        try:
            data = request(authenticated_service, start, end)
        except Exception as api_error:
            flash(f"An error occurred while making the API request: {str(api_error)}", 'danger')
            app.logger.error(f"API request error: {str(api_error)}")
            return redirect(url_for('home_page'))

        for dataset in data:
            table_name = dataset['columnHeaders'][0]['name']
            app.logger.debug("-------------------------")
            app.logger.debug(f"Table Name: {table_name}")
            app.logger.debug(f"Dataset: {dataset}")
            app.logger.debug(f"User ID: {user_id}")

            try:
                save_to_db(dataset, db, table_name, user_id)
            except SQLAlchemyError as e:
                db.session.rollback()
                flash(f"A database error occurred while saving data: {str(e)}", 'danger')
                app.logger.error(f"Database error: {str(e)}")
                return redirect(url_for('home_page'))

        flash("Data has been saved to the database.", 'success')

    except Exception as e:
        flash(f"An error occurred while requesting data: {str(e)}", 'danger')
        app.logger.error(f"General error: {str(e)}")

    finally:
        db.session.remove()

    return redirect(url_for('home_page'))
