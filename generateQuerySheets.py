import openai
import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up OpenAI API key
openai.api_key = "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"
# api_key = input("What's your openAPI key?")
# openai.api_key = api_key

def generate_query(prompt, table_structure):
    # Use the user's prompt and table structure to generate a query
    query_prompt = f"Write a query that will fulfill the user's request of {prompt} using the table structure {table_structure}"
    query = openai.Completion.create(
        engine="text-davinci-002", prompt=query_prompt, temperature=0.4, max_tokens=500)
    return query['choices'][0]['text']

# Set up API credentials - https://www.youtube.com/watch?v=vt_PtZ6KYIE
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Get the sheet by its name or URL
sheet_name = input("Please enter the URL of the Google Sheet: ")

# Get URL of the workbook.
wb = client.open_by_url(sheet_name)
# Enter your sheet name.
sheet_name = input("Please enter the sheet name:")
sheet1 = wb.worksheet(sheet_name)
original_df = sheet1.get_all_values()

# Get the data as a list of lists
data = sheet1.get_all_values()

# Convert the data to a pandas DataFrame
data = pd.DataFrame(data[1:], columns=data[0])

# Get the user's prompt
prompt = input("Ask away, what do you want to know?")
# Generate the query
query = generate_query(prompt, data.dtypes.to_string())
print(query)
