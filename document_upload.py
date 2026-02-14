import boto3
import json
import base64
import os



# API endpoint
conversation = "/document/upload_doc"


def lambda_handler(event, context):
    body = json.load(event['Body'])
    http_method = event['httpMethod']
    url_path = event["path"]

    if http_method == 'POST' and url_path == conversation:
        files = body.get('files')
        response = document_upload(files)
        return response
    

def document_upload(files):
    bucket_name = os.environ["bucket_name"]
    s3 = boto3.client('s3')

    try:
        for filename, value in files.item():
            value = base64.encode(value)

            s3.put_object(Body=value, Bucket=bucket_name, Key=filename)

        return "File Uploaded Successfully"
    

    except Exception as e:
        print(str(e))
        
        return "File Failed to upload"
