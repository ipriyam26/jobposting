import telegram
import openai_s
import google_sheets

# Replace YOUR_CHANNEL_NAME with the name of the channel you want to get messages from
channel_name = 'YOUR_CHANNEL_NAME'

# Get the messages from the Telegram channel
messages = telegram.get_messages(channel_name)

# Extract the job posts from the messages
job_posts = telegram.get_job_posts(messages)

# Structure the job posts using the OpenAI GPT-3 API
structured_job_posts = [
    openai_s.structure_job_post(job_post) for job_post in job_posts
]
# Update the Google Sheet with the structured job posts
google_sheets.update_sheet(structured_job_posts)