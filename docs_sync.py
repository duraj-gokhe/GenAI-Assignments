import boto3
import os
import json



def lambda_handler(event, context):
    body = json.load(event['Body'])

    # When document store in s3 bucket and event will trigger than this function will call and validate event.

    if body['resource'] == 's3' and body['event'] == 's3:upload':
        response = sync_documents()
        return response
    

# Sync Document - when new documents will upload in datasource like - s3 than this function will call and sync new document 
# in bedrock and store embedding in vector db

def sync_documents():
    client = boto3.client('bedrock-agent')

    response = client.start_ingestion_job(
    knowledgeBaseId= os.environ['knowledgebaseId'],   # knowledge base Id 
    dataSourceId= os.environ['datasourceId'],         # dataSource Id , which will be available in bedrock knowledge base after creations
    description='Sync documents for datasource'
    )
    
    return response
    