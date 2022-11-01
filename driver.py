import os
#import httplib2

from apiclient import discovery
from google.oauth2 import service_account
import WeeklyOdds
import OddsScraper


#initialize OddsScrapers
odds_scraper = OddsScraper.OddsScraper()

#Scrape web page
odds_scraper.scrape()
try:
    #connect to google api, specifically the google sheets api
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
    secret_file = os.path.join(os.getcwd(), 'service_creds.json')

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    service = discovery.build('sheets', 'v4', credentials=credentials)

    #specificy the spreadsheet that we will be editing
    spreadsheet_id = '1i26d9d9UX9S9wqxNeW4uI6MLerSO-vJA6aTJKbHIfGc'
    range_name = 'Odds!A2:D17'
    
    #intialize weekly odds
    weekly_odds = WeeklyOdds.WeeklyOdds()
    #get odds
    odds = weekly_odds.odds

    #get odds data
    values =[]
    for index, row, in odds.iterrows():
        list_row = row.tolist()[1:]
        print(list_row)
        values.append(list_row)
    print(values)

    #update values in the data dict that will be sent in the body of the sheets api request
    data = {
       'values' : values
    }

    print(data)
    #execute sheets api request to update values cells.
    service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()
    
except OSError as e:
    print(e)