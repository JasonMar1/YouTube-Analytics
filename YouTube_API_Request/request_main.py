from YouTube_API_Request.auth import get_authenticated_service
from data_processor import save_to_db
from YouTube_API_Request.api_requests import request

if __name__ == '__main__':
    authenticated_service = get_authenticated_service()
    start = '2023-01-01'
    end = '2024-01-01'
    #data = day_request(authenticated_service, start, end)

    data = request(authenticated_service, start, end)


    for i in data:
        table_name = i['columnHeaders'][0]['name']
        save_to_db(i, 'youtube_analytics.db', f'{table_name}')







    print("Data has been saved to the databases.")
