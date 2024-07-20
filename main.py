import os
import json
import pickle
import sqlite3
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

CLIENT_SECRETS_FILE = 'client_secret_70557108520-r25j4i26rba5bgd0q3dofcinqefh52oj.apps.googleusercontent.com.json'
SCOPES = [
    'https://www.googleapis.com/auth/yt-analytics.readonly',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtubepartner',
    'https://www.googleapis.com/auth/youtubepartner-channel-audit'
]
API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'

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

def execute_api_request(client_library_function, **kwargs):
    response = client_library_function(
        **kwargs
    ).execute()
    return response

def save_to_db(data, db_name, table_name, primary_key):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    column_headers = [header['name'] for header in data['columnHeaders']]
    columns = ', '.join([f"{header} TEXT" if header == primary_key else f"{header} INTEGER" for header in column_headers])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns}, PRIMARY KEY({primary_key}))")

    rows = data['rows']
    for row in rows:
        placeholders = ', '.join(['?' for _ in row])
        cursor.execute(f"INSERT OR IGNORE INTO {table_name} ({', '.join(column_headers)}) VALUES ({placeholders})", tuple(row))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    youtubeAnalytics = get_authenticated_service()

    metrics = ','.join([
        'annotationClickThroughRate',
        'annotationCloseRate',
        'averageViewDuration',
        'comments',
        'dislikes',
        'estimatedMinutesWatched',
        'estimatedRevenue',
        'likes',
        'shares',
        'subscribersGained',
        'subscribersLost',
        'viewerPercentage',
        'views',
        'playlistViews',
        'redViews',
        'estimatedRedMinutesWatched',
        'averageViewPercentage',
        'videosAddedToPlaylists',
        'videosRemovedFromPlaylists',
        'averageTimeInPlaylist',
        'playlistAverageViewDuration',
        'playlistEstimatedMinutesWatched',
        'playlistSaves',
        'playlistStarts',
        'viewsPerPlaylistStart',
        'annotationImpressions',
        'annotationClickableImpressions',
        'annotationClicks',
        'annotationClosableImpressions',
        'annotationCloses',
        'cardImpressions',
        'cardClicks',
        'cardClickRate',
        'cardTeaserImpressions',
        'cardTeaserClicks',
        'cardTeaserClickRate',
        'averageConcurrentViewers',
        'peakConcurrentViewers',
        'audienceWatchRatio',
        'relativeRetentionPerformance',
        'startedWatching',
        'stoppedWatching',
        'totalSegmentImpressions'
    ])

    dimensions_list = [
        'ageGroup',
        'channel',
        'country',
        'day',
        'gender',
        'month',
        'sharingService',
        'uploaderType',
        'video'
    ]

    # First API request for specific date range
    data = execute_api_request(
        youtubeAnalytics.reports().query,
        ids='channel==MINE',
        startDate='2023-01-01',
        endDate='2023-03-31',
        metrics=metrics,
        dimensions='day',
        sort='day'
    )

    # Save first dataset to 'youtube_analytics.db'
    save_to_db(data, 'youtube_analytics.db', 'analytics', 'day')

    # Second API requests for each dimension for lifetime data
    for dimension in dimensions_list:
        lifetime_data = execute_api_request(
            youtubeAnalytics.reports().query,
            ids='channel==MINE',
            startDate='2023-01-01',  # Assuming this is a date before any data would be available
            endDate='2024-12-31',  # Use a valid and recent date range
            metrics=metrics,
            dimensions=dimension,  # Use a single dimension to avoid conflicts
            sort='day'
        )

        save_to_db(lifetime_data, 'whole.db', f'analytics_{dimension}', dimension)

    print("Data has been saved to the databases.")



