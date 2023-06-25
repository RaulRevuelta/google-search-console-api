# Google Search Console Data Extractor

This Python script allows you to extract data from the Google Search Console API based on your specified parameters. It retrieves data for the selected time period and website property.

## Prerequisites

Before using the script, make sure you have completed the following steps:

1. Create credentials (OAuth client ID) on the Google Cloud Console.
2. Obtain the Client ID and Client Secret from the created credentials.

## Setup

1. Clone or download this repository.

2. Install the required dependencies listed in the `requirements.txt` file.

3. Open the `script.py` file.

4. Update the following variables in the script:

   - `client_id`: Replace with your OAuth client ID.
   - `client_secret`: Replace with your OAuth client secret.
   - `property_url`: Replace with the URL of the website property you want to extract data for.
   - `startDate` and `endDate`: Specify the desired time period for data extraction.
   - `dimensions`: Add or modify the dimensions you want to extract.

## Usage

Once executed, the script will extract the data based on the specified parameters and save it to a CSV file named `data.csv` in the same directory as the script.

## Notes

- Ensure that the necessary API access and permissions are granted for the Google Search Console API.
- The extracted data can be used for various purposes, such as SEO analysis, keyword research, and performance tracking.