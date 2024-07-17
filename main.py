#!/usr/bin/python

# Create a reporting job for the authenticated user's channel or
# for a content owner that the user's account is linked to.
# Usage example:
# python create_reporting_job.py --name='<name>'
# python create_reporting_job.py --content-owner='<CONTENT OWNER ID>'
# python create_reporting_job.py --content-owner='<CONTENT_OWNER_ID>' --report-type='<REPORT_TYPE_ID>' --name='<REPORT_NAME>'

import argparse
import os
from google.auth.transport.requests import Request
import pickle

import google.oauth2.credentials
import google_auth_oauthlib.flow
from debugpy._vendored.pydevd.pydev_sitecustomize.sitecustomize import input
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains

# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = 'client_secret_70557108520-r25j4i26rba5bgd0q3dofcinqefh52oj.apps.googleusercontent.com.json'
SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'

def auth():
  credentials = None
  # Check if the token.pickle file exists
  if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
      credentials = pickle.load(token)

  # If there are no valid credentials, go through the authorization flow
  if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
      credentials.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)
      credentials = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
      pickle.dump(credentials, token)

  return credentials


# Authorize the request and store authorization credentials.
def get_authenticated_service():
    credentials = auth()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)




def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()

  print(response)

if __name__ == '__main__':
    # Disable OAuthlib's HTTPs verification when running locally.
    # *DO NOT* leave this option enabled when running in production.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    youtubeAnalytics = get_authenticated_service()
    execute_api_request(
        youtubeAnalytics.reports().query,
        ids='channel==MINE',
        startDate='2021-01-03',
        endDate='2021-01-04',
        metrics='estimatedMinutesWatched,views,likes,subscribersGained,cardImpressions,subscribersLost,annotationImpressions',
        dimensions='day',
        sort='day'
    )