# auth.py
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from flask import session, redirect, url_for, request, flash
from app import db
from app.models import User
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
CLIENT_SECRETS_FILE = 'client_secret_70557108520-nvee7f4fus7n6pdm839venm3664vjb4v.apps.googleusercontent.com.json'
SCOPES = [
    'https://www.googleapis.com/auth/yt-analytics.readonly',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtubepartner',
    'https://www.googleapis.com/auth/youtubepartner-channel-audit'
]

def start_oauth_flow():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=url_for('oauth2callback', _external=True)
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    session['state'] = state
    return redirect(authorization_url)

def oauth2callback():
    state = session['state']
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        state=state,
        redirect_uri=url_for('oauth2callback', _external=True)
    )
    flow.fetch_token(authorization_response=request.url)

    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    # Save credentials to the user in the database
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            user.google_credentials = credentials_to_json(credentials)
            db.session.commit()
            return redirect(url_for('home_page'))
    else:
        flash('User session not found.', 'danger')
        return redirect(url_for('register_page'))

def get_authenticated_service(user_id):
    user = User.query.get(user_id)
    if not user or not user.google_credentials:
        return start_oauth_flow()

    credentials = json_to_credentials(user.google_credentials)

    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

        # Update the refreshed credentials in the database
        user.google_credentials = credentials_to_json(credentials)
        db.session.commit()

    return build('youtubeAnalytics', 'v2', credentials=credentials)

def credentials_to_json(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

def json_to_credentials(json_data):
    return Credentials(
        token=json_data['token'],
        refresh_token=json_data['refresh_token'],
        token_uri=json_data['token_uri'],
        client_id=json_data['client_id'],
        client_secret=json_data['client_secret'],
        scopes=json_data['scopes']
    )
