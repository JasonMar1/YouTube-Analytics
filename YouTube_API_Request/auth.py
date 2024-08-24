from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from flask import session, redirect, url_for, request, flash
from app import db
from app.models import User
import json
import os

# Environment setup to allow HTTP (for development purposes)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Path to the client secrets JSON file
CLIENT_SECRETS_FILE = '/app/app/client_secret_70557108520-nvee7f4fus7n6pdm839venm3664vjb4v.apps.googleusercontent.com.json'

# Scopes required for accessing YouTube data
SCOPES = [
    'https://www.googleapis.com/auth/yt-analytics.readonly',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtubepartner',
    'https://www.googleapis.com/auth/youtubepartner-channel-audit'
]

# Static redirect URI registered in the Google Cloud Console
REDIRECT_URI = 'https://youtube-analytics-dashboard-2ac54861e0a3.herokuapp.com/oauth2callback'

def start_oauth_flow():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url(
        include_granted_scopes='true'
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
        redirect_uri=REDIRECT_URI
    )
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials

    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            user.google_credentials = json.dumps(credentials_to_json(credentials))
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

    credentials = json_to_credentials(user.google_credentials)

    if credentials.expired:
        flash('The access token has expired. Please re-authenticate.', 'danger')
        return start_oauth_flow()

    return build('youtubeAnalytics', 'v2', credentials=credentials)

def credentials_to_json(credentials):
    """Converts Google OAuth2 Credentials object to a dictionary."""
    return {
        'token': credentials.token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

def json_to_credentials(json_data):
    """Converts a dictionary to a Google OAuth2 Credentials object."""
    return Credentials(
        token=json_data.get('token'),
        token_uri=json_data.get('token_uri'),
        client_id=json_data.get('client_id'),
        client_secret=json_data.get('client_secret'),
        scopes=json_data.get('scopes')
    )
