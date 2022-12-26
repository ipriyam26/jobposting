import re

import openai

def structure_job_post(job_post_text):
  """
  Use the OpenAI GPT-3 API to structure a job post.
  """
  # Set the OpenAI API key
  openai.api_key = "YOUR_OPENAI_API_KEY"

  # Use the OpenAI GPT-3 API to generate structured data for the job post
  prompt = (
      f"Please structure the following job post:\n{job_post_text}\n\n"
      f"Fields: Company, Subsidiary, Role, Last Date To Apply, Designation, Job Function, Stipend, Start Date, Internship, Duration, Application Link"
  )
  response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.7,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=1,
      presence_penalty=1
  )
  structured_data = response['choices'][0]['text']

  # Extract the structured data from the response
  structured_data_dict = {}
  field_names = ['Company', 'Subsidiary', 'Role', 'Last Date To Apply', 'Designation', 'Job Function', 'Stipend', 'Start Date', 'Internship', 'Duration', 'Application Link']
  for field in field_names:
    if match := re.search(f"{field}: (.*?)\n", structured_data):
      structured_data_dict[field] = match[1]
    else:
      structured_data_dict[field] = ""

  return structured_data_dict
