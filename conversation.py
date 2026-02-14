import boto3
import os
import json

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import JsonOutputParser
from langchain_aws import ChatBedrock
from langchain_aws import AmazonKnowledgeBasesRetriever

# API endpoint
conversation = "/chat/conversation"


def lambda_handler(event, context):
    body = json.load(event['Body'])
    http_method = event['httpMethod']
    url_path = event["path"]

    if http_method == 'POST' and url_path == conversation:
        query = body.get('query')
        response = conversation_kb(query)
        return response


def conversation_kb(query):

    # Amazon Bedrock - settings
    bedrock_runtime = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
    )

    # model_id we can pick from lambda
    model_id = os.environ['model_id']  # model_id will be fundation model id or arn we can use like - claude anthropic, amazon nova, titen

    model_kwargs =  { 
        "max_tokens": 2048,
        "temperature": 0.0,
        "top_k": 250,
        "top_p": 1,
        "stop_sequences": ["\n\nHuman"],
    }

    # LangChain - RAG chain with citations
    template = ''' you are a document assistant, provide response with document related 
                1. If some date or recent documents ask provide top records like - date wise filtering
                2. If documents response lenght is more than 500 words split it and send in chunks
                3. If documents not found in data source than No Documents available for this query related.'''

    prompt = ChatPromptTemplate.from_template(template)

    # Amazon Bedrock - KnowledgeBase Retriever 
    retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id= os.environ['knowledge_base_id'], # Set Knowledge base ID from bedrock knowledge base
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
    )

    model = ChatBedrock(
        client=bedrock_runtime,
        model_id=model_id,
        model_kwargs=model_kwargs,
    )

    chain = (
        RunnableParallel({"context": retriever, "question": RunnablePassthrough()}).assign(response = prompt | model | JsonOutputParser())
        .pick(["response", "context"])
    )   

    response = chain.invoke(query)

    output = response['response']['text']
    citation = response['response']['citation']

    return {"response": output, "citation":citation}
