
# YouTube Analytics Web App

## Overview

This web application allows YouTube content creators to access detailed performance analytics of their videos by connecting directly to the YouTube API. After registering and linking their YouTube account, users can view key performance metrics based on a custom date range, with options to filter analytics by day, month, and device type, and choose specific metrics such as views, watch time, and subscribers.

### Features

- **Custom Date Range Analysis**: Analyze data for any selected time period.
- **Detailed Breakdown**:
  - **Day View**: See daily statistics for views, subscribers, and more.
  - **Month View**: Summarize performance on a monthly basis.
  - **Device Type View**: Understand audience behavior based on the devices used (mobile, desktop, etc.).
- **Metrics Filtering**: Choose which metrics to display, offering flexible reporting (e.g., views, subscribers, watch time).
  
## Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **APIs**: YouTube Analytics API
- **Authentication**: OAuth2 (Google)
- **Deployment**: (Coming Soon)

> **Note**: The app is currently available **only locally** as we are in the process of migrating the application back online due to issues with the Heroku platform.

## Usage

1. **Register/Login**: 
   - Users need to register and authenticate with their Google/YouTube account.
   
2. **Connect YouTube**:
   - After logging in, connect your YouTube account to fetch your channel's analytics.

3. **Request Data**:
   - Select a date range for the analytics data you want to view, and fetch the data for that specific period.

4. **View Analytics**:
   - Navigate through the app to see daily, monthly, or device-based reports.
   - Use filters to select the metrics you wish to view (e.g., views, watch time, likes).

## File Structure

Here’s a brief overview of the important files in the project:

- `create_app.py`: Initializes the Flask app and sets up routing, database, and extensions.
- `routes.py`: Defines the app’s routes and handles API requests for analytics data.
- `api_requests.py`: Handles requests to the YouTube API using the authenticated service. It includes functions for retrieving analytics data like `deviceType`, `day` etc. This module checks metric availability and fetches data for different dimensions.
- `auth.py`: Manages the OAuth 2.0 flow with Google for authenticating YouTube accounts. It handles token refreshing, saving credentials to the database, and redirecting users during the OAuth process.
- `request_main.py`: The main request handler. This file ties together authenticated YouTube API requests, processes the data, and stores it into the PostgreSQL database. It also includes session checks to ensure user authentication.
- `data_processor.py`: Processes the YouTube analytics data received from API requests and saves it to the database. It contains logic to map API response data to database models like `DeviceType`, `Day` and more.

## API Documentation

This app uses the **YouTube Analytics API** to retrieve data. Key functionalities include:
- Fetching detailed reports from the YouTube Analytics API.
- Accessing authenticated users' YouTube channels and their video performance data.

More information about the API can be found in the [YouTube Analytics API documentation](https://developers.google.com/youtube/analytics/).

## Demo Video

To see the YouTube Analytics Web App in action, watch the video below:

[[YouTube Analytics Web App Demo]](https://youtu.be/rvmNxopD9LU)

