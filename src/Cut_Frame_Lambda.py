import boto3
import os
import sys
import uuid
from PIL import Image, ImageFilter

s3_client = boto3.client('s3')

TMP = "/tmp/"
FILE_NAME_INDEX = 2

def augmentation_image(file_name, image_path):
    result_file_path = []

    with Image.open(image_path) as image:
        tmp = image 
        result_path = "resized-"+file_name       
        image.thumbnail((128, 128))
        result_path = TMP+result_path
        image.save(result_path)
        result_file_path.append(result_path)
    return result_file_path

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print "bucket name : " + str(bucket)
        print "key : " + str(key)
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)

        s3_client.download_file(bucket, key, download_path)
        file_name = key
        result_path = augmentation_image(file_name, download_path)
        print result_path
        for upload_path in result_path:
            s3_client.upload_file(upload_path, 'result-image-data-augmentation', upload_path.split("/")[FILE_NAME_INDEX])