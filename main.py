import os
from auth import get_authenticated_service
from data_processor import db_from_json,save_to_db
from api_requests import day_request, device_type_request, request

if __name__ == '__main__':
    authenticated_service = get_authenticated_service()
    start = '2023-01-01'
    end = '2024-01-01'
    #data = day_request(authenticated_service, start, end)
    device_data = request(authenticated_service,start,end)
    print(device_data)
    for data in device_data:
        print(data)
        #save_to_db(device_data, 'youtube_analytics.db', f'{data}')







    print("Data has been saved to the databases.")
