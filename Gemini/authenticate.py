import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from Loggs import logger

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']
CLIENT_SECRETS_FILE = "jsons/client_secret.json"


def authenticate_gemini():
    '''
    Функция авторизации для gemini
    '''
    creds = None
    if os.path.exists('jsons/gemini_token.json'):
        creds = Credentials.from_authorized_user_file('jsons/gemini_token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open('jsons/gemini_token.json', 'w') as token:
            token.write(creds.to_json())
    
    logger.info("Авторизация в gemini Прошла успешно!")
    return creds