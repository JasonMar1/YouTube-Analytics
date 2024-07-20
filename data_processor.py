import json
import sqlite3

# Load the JSON data from the file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the column headers (not used directly in this approach)
column_headers = [header['name'] for header in data['columnHeaders']]

# Extract the rows of data
rows = data['rows']

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('youtube_analytics.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS analytics (
        day TEXT PRIMARY KEY,
        estimatedMinutesWatched INTEGER,
        views INTEGER,
        likes INTEGER,
        subscribersGained INTEGER,
        cardImpressions INTEGER,
        subscribersLost INTEGER,
        annotationImpressions INTEGER
    )
''')

# Insert new rows into the database
for row in rows:
    cursor.execute('''
        INSERT OR IGNORE INTO analytics (
            day, estimatedMinutesWatched, views, likes, subscribersGained,
            cardImpressions, subscribersLost, annotationImpressions
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', tuple(row))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Data has been saved to the database.")
