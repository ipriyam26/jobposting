import json
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def update_google_sheet(job_posts):
  """
  Update a Google Sheet with the specified job posts.
  """
  # Set the path to the JSON file containing your Google Sheets API credentials
  json_file_path = os.path.join('google_sheets_credentials.json')

  # Load the credentials from the JSON file
  credentials = Credentials.from_authorized_user_info(info=json.load(open(json_file_path)))

  # Build the Sheets API service
  sheets_service = build('sheets', 'v4', credentials=credentials)

  # Replace YOUR_SPREADSHEET_ID with the ID of the Google Sheet you want to update
  spreadsheet_id = 'YOUR_SPREADSHEET_ID'

  # Set the field names for the Google Sheet
  field_names = ['Company', 'Subsidiary', 'Role', 'Last Date To Apply', 'Designation', 'Job Function', 'Stipend', 'Start Date', 'Internship', 'Duration', 'Application Link']

  # Append the job posts to the Google Sheet
  for job_post in job_posts:
    # Create a row for the job post
    row = [job_post[field] for field in field_names]

    # Append the row to the Google Sheet
    sheets_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range='A1',  # Append the row to the first column of the sheet
        insertDataOption='INSERT_ROWS',
        valueInputOption='RAW',
        body={'values': [row]}
    ).execute()
