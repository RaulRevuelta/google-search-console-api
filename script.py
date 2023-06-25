from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow
from oauth2client.file import Storage
from googleapiclient.discovery import build
import os
import pandas as pd

# Google Cloud Project Client ID & Client Secrets
client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'
oauth_scope = 'https://www.googleapis.com/auth/webmasters.readonly'
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

# Create the OAuth2WebServerFlow instance
flow = OAuth2WebServerFlow(client_id, client_secret, oauth_scope, redirect_uri)

# Path to store the credentials
credentials_path = 'credentials.dat'

if os.path.exists(credentials_path):
    # Load credentials from file
    storage = Storage(credentials_path)
    credentials = storage.get()
else:
    # Run the OAuth flow with automated code retrieval
    credentials = run_flow(flow, Storage(credentials_path))

# Build the service
service = build('searchconsole', 'v1', credentials=credentials)

# Select property, start date and end date
# https://developers.google.com/webmaster-tools/v1/searchanalytics/query
property_url = 'https://example.com/'
startDate = '2020-01-01'
endDate = '2020-12-31'
dimensions = ['date', 'page', 'query']

# Create an empty list to store the rows retrieved from the response
data = []

# Initialize the variable 'startRow' to track the starting row of each request
startRow = 0

while startRow == 0 or startRow % 25000 == 0:
    # Build the request body with the specified variables
    request = {
        'startDate': startDate,
        'endDate': endDate,
        'dimensions': dimensions,
        'rowLimit': 25000,
        'startRow': startRow
    }

    # Store the response from the Google Search Console API
    response = service.searchanalytics().query(siteUrl=property_url, body=request).execute()

    # Get and update the rows
    rows = response.get('rows', [])
    startRow = startRow + len(rows)

    # Extend the data list with the rows
    data.extend(rows)

# Create a DataFrame from the data list
df = pd.DataFrame([
    {
        'date': row['keys'][0],
        'page': row['keys'][1],
        'query': row['keys'][2],
        'clicks': row['clicks'],
        'impressions': row['impressions'],
        'ctr': row['ctr'],
        'position': row['position']
    } for row in data
])

# Save the DataFrame as a CSV file
df.to_csv('data.csv')