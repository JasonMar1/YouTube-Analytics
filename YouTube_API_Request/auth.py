from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle
import os

CLIENT_SECRETS_FILE = 'client_secret_70557108520-r25j4i26rba5bgd0q3dofcinqefh52oj.apps.googleusercontent.com.json'
API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'

SCOPES = [
    'https://www.googleapis.com/auth/yt-analytics.readonly',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtubepartner',
    'https://www.googleapis.com/auth/youtubepartner-channel-audit'
]

def auth():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return credentials


def get_authenticated_service():
    credentials = auth()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)