import os

import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from Loggs import logger

CLIENT_SECRETS_FILE = "jsons/client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']


# Функция для получения авторизованного сервиса YouTube API
def authenticate_youtube():
    credentials = None

    # Попробуйте загрузить сохраненные учетные данные из файла
    if os.path.exists('jsons/youtube_token.json'):
        credentials = Credentials.from_authorized_user_file('jsons/youtube_token.json', SCOPES)

    # Если нет учетных данных или они истекли, выполните авторизацию
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        
        # Сохраните учетные данные в файл для последующего использования
        with open('jsons/youtube_token.json', 'w') as token_file:
            token_file.write(credentials.to_json())
    
    # Создайте и верните экземпляр сервиса YouTube API
    logger.info("Авторизация в Youtube прошла успешно!")
    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)