from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from YouTube_API_Request.auth import get_authenticated_service
import googleapiclient

all_dimensions = [
    'deviceType',
    'day',
    'gender',
    'month',
    'sharingService',
    'uploaderType',
    'video'
]

all_metrics = [
    'views',
    'adImpressions',
    'annotationClickableImpressions',
    'annotationClicks',
    'annotationClickThroughRate',
    'annotationClosableImpressions',
    'annotationCloses',
    'annotationCloseRate',
    'annotationImpressions',
    'audienceWatchRatio',
    'averageViewDuration',
    'averageViewPercentage',
    'cardClickRate',
    'cardClicks',
    'cardImpressions',
    'cardTeaserClickRate',
    'cardTeaserClicks',
    'cardTeaserImpressions',
    'comments',
    'cpm',
    'dislikes',
    'estimatedMinutesWatched',
    'likes',
    'playbackBasedCpm',
    'playlistStarts',
    'savesAdded',
    'savesRemoved',
    'shares',
    'subscribersGained',
    'subscribersLost',
    'videosAddedToPlaylists',
    'videosRemovedFromPlaylists',
    'viewerPercentage'
]


def execute_api_request(client_library_function, **kwargs):
    response = client_library_function(
        **kwargs
    ).execute()
    return response


def check_metric_availability(authenticated_service, startDate, endDate, dimension):
    available_metrics = []
    for metric in all_metrics:
        try:
            execute_api_request(
                authenticated_service.reports().query,
                ids='channel==MINE',
                startDate=startDate,
                endDate=endDate,
                metrics=metric,
                dimensions=dimension
            )
            available_metrics.append(metric)
        except googleapiclient.errors.HttpError as e:
            print("")
            # print(f"Metric {metric} is not available: {e}")
    return available_metrics


def check_availability(authenticated_service, startDate, endDate, dimension):
    try:
        execute_api_request(
            authenticated_service.reports().query,
            ids='channel==MINE',
            startDate=startDate,
            endDate=endDate,
            metrics='views',  # Using a common metric to check dimension availability
            dimensions=dimension,
        )
        return True
    except googleapiclient.errors.HttpError as e:
        # print(f"Dimension {dimension} is not available: {e}")
        return False


def request(authenticated_service, startDate, endDate):
    allData = []
    for dimension in all_dimensions:
        print(dimension)
        if check_availability(authenticated_service, startDate, endDate, dimension):
            available_metrics = check_metric_availability(authenticated_service, startDate, endDate, dimension)
            metrics = ','.join(available_metrics)
            data = execute_api_request(
                authenticated_service.reports().query,
                ids='channel==MINE',
                startDate=startDate,
                endDate=endDate,
                metrics=metrics,
                dimensions=dimension
            )
            allData.append(data)
    return allData


def day_request(authenticated_service, startDate, endDate):
    available_metrics = check_metric_availability(authenticated_service, startDate, endDate)
    metrics = ','.join(available_metrics)
    data = execute_api_request(
        authenticated_service.reports().query,
        ids='channel==MINE',
        startDate=startDate,
        endDate=endDate,
        metrics=metrics,
        dimensions='day',
        sort='day'
    )
    return data


def device_type_request(authenticated_service, startDate, endDate):
    available_metrics = check_metric_availability(authenticated_service, startDate, endDate)

    metrics = ','.join(available_metrics)
    data = execute_api_request(
        authenticated_service.reports().query,
        ids='channel==MINE',
        startDate=startDate,
        endDate=endDate,
        metrics='views',
        dimensions='deviceType'
    )
    return data


# date format =  startDate='2023-01-01',

def country_request(authenticated_service, startDate, endDate):
    available_metrics = check_metric_availability(authenticated_service, startDate, endDate)

    metrics = ','.join(available_metrics)
    data = execute_api_request(
        authenticated_service.reports().query,
        ids='channel==MINE',
        startDate=startDate,
        endDate=endDate,
        metrics='views',
        dimensions='deviceType',
    )
    return data

    """
    # Second API requests for each dimension for lifetime data
    for dimension in dimensions_list:
        try:
            print(dimension)
            lifetime_data = execute_api_request(
                youtubeAnalytics.reports().query,
                ids='channel==MINE',
                startDate='2023-01-01',  # Assuming this is a date before any data would be available
                endDate='2024-12-01',  # Use a valid and recent date range
                metrics=metrics,
                dimensions='subscribedStatus',  # Use a single dimension to avoid conflicts
            )
            print(lifetime_data)
        except:
            print('')

        # save_to_db(lifetime_data, 'whole.db', f'analytics_{dimension}', dimension)
    """
