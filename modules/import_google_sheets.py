# -*- coding: utf-8 -*-
import os.path
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

FIRST = 0
AUTH_SCOPES = ["https://www.googleapis.com/auth/drive"]


def authorize_to_api(scope):
    """
    Authorize Scraper API to the Google APIs suite (Drive)
    """
    credentials = None
    if os.path.exists("./credentials/token.json"):
        credentials = Credentials.from_authorized_user_file(
            "./credentials/token.json", scope)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            application_flow = InstalledAppFlow.from_client_secrets_file(
                "./credentials/credentials.json", scope)
            credentials = application_flow.run_local_server(port=0)
        with open("./credentials/token.json", mode="w") as token:
            token.write(credentials.to_json())
    print "Authorization successful!"
    return credentials


def handle_spreadsheet(credentials):
    """
    Check for the existing results spreadsheet
    and create new if missing
    """
    try:
        service_drive = build(serviceName="drive", version="v3", credentials=credentials)
        print "Connection to GoogleDrive established!"
        search_results = service_drive.files().list(q="name='ScraperResults'").execute()
        files = search_results.get("files")
        if files:
            file_ = files[FIRST]
            print "File: {0} exists!".format(file_.get("name"))
        else:
            file_body = {'name': 'ScraperResults', 'mimeType': 'application/vnd.google-apps.spreadsheet'}
            file_ = service_drive.files().create(body=file_body, fields="id").execute()
            print "File: ScraperResults created!"
        return file_.get("id")
    except HttpError as err:
        print "Error: {0}".format(err)


def handle_values(recipe):
    """
    Parse data from Recipe object
    """
    products = ""
    for product in recipe.products:
        products += str(product.title.encode("utf-8"))
        products += str(product.quantity.encode("utf-8")) + "\n"

    values = [
        [
            u"Име на рецепта: ", recipe.title
        ],
        [
            u"Продукти: ", products
        ],
        [
            u"Готвач: ", recipe.chef.name
        ],
        [
            u"Рейтинг на готвача: ", recipe.chef.get_ratings()
        ],
        [
            u"Рейтинг на рецепта: ", recipe.rating
        ],
        [
            time.asctime()
        ]
    ]
    return values


def upload_to_sheets(credentials, sheet_id, values):
    """
    Upload ValueRange object data to GoogleSheet's spreadsheet
    """
    try:
        service_sheets = build(serviceName="sheets", version="v4", credentials=credentials)
        values_body = {"values": values}
        sheet = service_sheets.spreadsheets().values().append(
            spreadsheetId=sheet_id, range="Sheet1!A:A",
            valueInputOption="RAW", insertDataOption="INSERT_ROWS",
            body=values_body).execute()
        print('{0} cells appended.'.format(sheet
                                           .get('updates')
                                           .get('updatedCells')))
    except HttpError as err:
        print "Error: {0}".format(err)
