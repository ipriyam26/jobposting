import json
import os
import re
import time
from telethon import TelegramClient
from telethon.errors import FloodWaitError

# Set the API ID and hash for the Telegram client
api_id = 12345
api_hash = 'abcdefghijklmnopqrstuvwxyz'

# Set the path to the JSON file containing your Telegram API credentials
json_file_path = os.path.join('telegram_credentials.json')

# Load the credentials from the JSON file
credentials = json.load(open(json_file_path))

# Create a Telegram client using the API ID, API hash, and credentials
client = TelegramClient('session_name', api_id, api_hash, **credentials)

def get_messages(channel_name):
  """
  Get a list of messages from a Telegram channel.
  """
  # Start the client
  client.start()

  # Get the channel object for the channel
  channel = client.get_entity(channel_name)

  # Get the messages from the channel
  messages = []
  offset_id = 0
  while True:
    try:
      messages.extend(client.get_messages(channel, offset_id=offset_id))
      offset_id = messages[-1].id
    except FloodWaitError as e:
      print(f"Waiting {e.seconds} seconds before continuing...")
      time.sleep(e.seconds)
      continue
    except Exception:
      break

  # Stop the client
  client.stop()

  return messages

def get_job_posts(messages):
  """
  Extract job posts from a list of messages.
  """
  return [
      message.message[len('job posting:'):].strip() for message in messages
      if message.message.lower().startswith('job posting:')
  ]
