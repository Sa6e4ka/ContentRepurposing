import json

from dotenv import load_dotenv
import os
load_dotenv()

client_id = os.environ.get("GOOGLE_CLIENT_ID")
client_secret = os.environ.get("GOOGLE_CLIENT_SECRETS")
project_id = os.environ.get("GOOGLE_PROJECT_ID")

host = "http://localhost:8080/"

# Здесь должен быть список эндпоинтов перенаправления - нужно их добавить в redirect URIs в настройках приложения в google cloud console (только при web app (nvm)) 
redirect_uris = [
    "http://localhost"
]

def create_secrerts(
        client_id: str,
        client_secret: str,
        project_id: str,
        redirect_uris: list
):
    '''Создание json-файла с сектретами пользователя'''

    DATA = {
        "installed": {
            "client_id": client_id,
            "project_id": project_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": client_secret,
            "redirect_uris": redirect_uris
        }
    }

    with open("jsons/client_secret.json", "w", encoding="utf-8") as secrets:
        json.dump(DATA, secrets, ensure_ascii=False, indent=4)

# Вызов функции
# create_secrerts(
#     client_id=client_id,
#     client_secret=client_secret,
#     project_id=project_id,
#     redirect_uris=redirect_uris
# )