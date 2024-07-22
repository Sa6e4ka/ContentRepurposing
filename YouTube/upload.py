from googleapiclient.http import MediaFileUpload
from Loggs import logger


def upload_video(youtube, file, title, description, publ):
    '''
    Функция исключительно для #загрузки# видео на YouTube
    '''

    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': [
                "memes", 
                "funny", 
                "dank memes", 
                "lol",
                "hilarious", 
                "viral", 
                "trending", 
                "lmao",
                "memevideo",
                "laugh"
            ],
        },
        'status': {
            'privacyStatus': 'private',
            'publishAt': publ,
        }
    }
    media_file = MediaFileUpload(file)
    youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    ).execute()



