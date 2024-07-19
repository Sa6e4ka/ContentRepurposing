from googleapiclient.http import MediaFileUpload
from Loggs import logger


def upload_video(youtube, file, title, description, tags, publ):
    '''
    Функция исключительно для #загрузки# видео на YouTube
    '''

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

    logger.info("Video id '%s' was successfully uploaded." % response_upload["id"])


