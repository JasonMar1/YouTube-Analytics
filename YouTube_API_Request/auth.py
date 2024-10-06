from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from flask import session, redirect, url_for, request, flash
from app import db, app
from app.models import User
import json
import os

# Environment setup to allow HTTP (for development purposes)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Path to the client secrets JSON file
CLIENT_SECRETS_FILE = ('/app/app/client_secret_70557108520-nvee7f4fus7n6pdm839venm3664vjb4v.apps.googleusercontent.com'
                       '.json')



# Scopes required for accessing YouTube data
SCOPES = os.getenv('SCOPES')

# Static redirect URI registered in the Google Cloud Console
REDIRECT_URI = 'https://youtube-analytics-dashboard-2ac54861e0a3.herokuapp.com/oauth2callback'


def start_oauth_flow():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI  # Static redirect URI
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',  # Ensures that a refresh token is received
        include_granted_scopes='true',
        # Prevents the user from being prompted again if they already granted permissions
        prompt='consent'
    )
    session['state'] = state
    return redirect(authorization_url)


def oauth2callback():
    state = session.get('state')
    if not state:
        flash("State parameter missing or session expired.", "danger")
        return redirect(url_for('home_page'))

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        state=state,
        redirect_uri=REDIRECT_URI  # Static redirect URI
    )

    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials

    # Log the credentials to debug
    app.logger.debug(f"Token: {credentials.token}")
    app.logger.debug(f"Refresh Token: {credentials.refresh_token}")
    app.logger.debug(f"Token URI: {credentials.token_uri}")
    app.logger.debug(f"Client ID: {credentials.client_id}")
    app.logger.debug(f"Client Secret: {credentials.client_secret}")

    if not credentials.refresh_token:
        flash("Failed to obtain refresh token. Please try again.", "danger")
        return redirect(url_for('google_signup'))

    # Save credentials to the user's record in the database
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            user.google_credentials = json.dumps(credentials_to_json(credentials))  # Serialize to JSON string
            db.session.commit()
            flash("Authentication successful.", "success")
            return redirect(url_for('home_page'))
    else:
        flash('User session not found.', 'danger')
        return redirect(url_for('register_page'))


def get_authenticated_service(user_id):
    user = User.query.get(user_id)
    if not user or not user.google_credentials:
        return start_oauth_flow()

    credentials = json_to_credentials(user.google_credentials)  # Deserialize from JSON string
    # flash(credentials.refresh_token, category='danger')  # Flashes refresh_token value

    if credentials.expired and credentials.refresh_token:
        try:
            credentials.refresh(Request())
        except Exception as e:
            print(f"Error refreshing credentials: {e}")
            return start_oauth_flow()

        # Update the refreshed credentials in the database
        user.google_credentials = json.dumps(credentials_to_json(credentials))  # Serialize to JSON string
        db.session.commit()

    return build('youtubeAnalytics', 'v2', credentials=credentials)


def credentials_to_json(credentials):
    """Converts Google OAuth2 Credentials object to a dictionary."""
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }


def json_to_credentials(json_data):
    """Converts a dictionary to a Google OAuth2 Credentials object."""
    return Credentials(
        token=json_data.get('token'),
        refresh_token=json_data.get('refresh_token'),
        token_uri=json_data.get('token_uri'),
        client_id=json_data.get('client_id'),
        client_secret=json_data.get('client_secret'),
        scopes=json_data.get('scopes')
    )
