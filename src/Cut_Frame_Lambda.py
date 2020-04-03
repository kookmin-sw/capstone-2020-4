import boto3
import os
import sys
import uuid
import cv2

s3_client = boto3.client('s3')

TMP = "/tmp/"
FILE_PATH_INDEX = 0
FILE_NAME_INDEX = 2

def video_processing(file_name, video_path):
    result_file_path = []

    video = cv2.VideoCapture(video_path)
    idx = 0

    while(video.isOpened()):
        ret, frame = video.read()
        width = video.get(3)
        height = video.get(4)

        if idx == 100:
            break

        if ret < 0:
            break

        frame = cv2.resize(frame, (720, 480))
        result_path = video_path.split(".")[FILE_PATH_INDEX]+str(idx)+".jpg"
        result_file_path.append(result_path)

        cv2.imwrite(result_path, frame)

        idx += 1

    video.release()
    print ("Video Processing Done ...")
    return result_file_path

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)

        s3_client.download_file(bucket, key, download_path)
        file_name = key

        result_path = video_processing(file_name, download_path)

        for upload_path in result_path:
            s3_client.upload_file(upload_path, 'test7868-resized', upload_path.split("/")[FILE_NAME_INDEX])

        print ("S3 Upload Done ...")

