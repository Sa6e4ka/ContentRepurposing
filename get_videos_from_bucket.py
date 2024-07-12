import boto3
from botocore.exceptions import ClientError
import os
import json
from dotenv import load_dotenv
import argparse

load_dotenv()

class S3Client:
    def __init__(self, access_key: str, secret_key: str, bucket_name: str):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
        }
        self.bucket_name = bucket_name
        self.client = boto3.client("s3", **self.config)

    def get_file(self, object_name: str, destination_path: str):
        try:
            response = self.client.get_object(Bucket=self.bucket_name, Key=object_name)
            data = response["Body"].read()
            with open(destination_path, "wb") as file:
                file.write(data)
            print(f"File {object_name} downloaded to {destination_path}")
        except ClientError as e:
            print(f"Error downloading file: {e}")

def main():
    if args.clear: 
        clear_dir('videos/')
        exit()
    with open('vid.json') as file:
        json_data = json.load(file)
        ids = [idd for idd in json_data]

    s3_client = S3Client(
        access_key=os.environ.get("AWS_ACCESS_KEY"),
        secret_key=os.environ.get("AWS_SECRET_KEY"),
        bucket_name=os.environ.get("AWS_BUCKET_NAME"),
    )

    for item in ids:
        name = f"{item}.mp4"
        s3_client.get_file(object_name=name, destination_path=f"videos/{name}")

def clear_dir(path: str):
    if not os.path.exists(path):
        print(f"Директория {path} не существует.")
        return
    
    files = os.listdir(path)
    
    for file in files:
        file_path = os.path.join(path, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Файл {file_path} удален успешно.")
            else:
                print(f"Путь {file_path} не указывает на файл.")
        except Exception as e:
            print(f"Ошибка при удалении файла {file_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clear a directory")
    parser.add_argument("--clear", action="store_true", help="Clear the directory")
    args = parser.parse_args()
    main()
