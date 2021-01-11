from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find spreadsheet and open spreadsheet based on sheet_info.txt
with open("sheet_info.txt", "r") as f:
    data = f.readlines()
    spreadsheet_name = data[0].rstrip("\n")
    sheet_index = int(data[1])
spreadsheet = client.open(spreadsheet_name)
sheet = spreadsheet.get_worksheet(sheet_index)

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
pprint(list_of_hashes)
