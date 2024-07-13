import os
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload
from oauth2client.file import Storage


CLIENT_SECRETS_FILE = "client_secrets.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']



def get_authenticated_service(cred_file_name):
    credential_path = os.path.join('./', cred_file_name)
    store = Storage(credential_path)
    credentials = store.get()

    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

def upload(name,title="memes i found on the internet",description="dank memes, dank, meme, memes, edgy, dankest, funny af, offensive memes, meme compilation, dank meme compilation",tags=["memes", "funnymoments", "compilation", "unusualmemes", "tiktoks", "tiktokmemes"],cr_fl_name='credential_secrets.json',publishat='2025-07-27T11:20:00.0Z'):
    try:
        youtube = get_authenticated_service(cr_fl_name)

        file_path = f"videos/{name}"
        title = title
        description = description
        tags = tags


        upload_video(youtube, file_path, title, description, tags,publ=publishat)

    except googleapiclient.errors.HttpError as e:
        error_message = e._get_reason()
        print(f"Произошла ошибка при загрузке видео: {error_message}")
        return
    
def upload_video(youtube, file, title, description, tags,publ):

    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,

        },
        'status': {
            'privacyStatus': 'private',
            'publishAt': publ,
        }
    }
    media_file = MediaFileUpload(file)
    response_upload = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    ).execute()

    print("Video id '%s' was successfully uploaded." % response_upload["id"])


def main():
    upload('7366694126634437921.mp4',cr_fl_name='credential_secrets.json')

if __name__ == "__main__":
    main()