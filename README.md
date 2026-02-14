**CONVERSATIONAL AI BOT**

Conversational AI bot for own documents with RAG and Embedding vector

################################ **Files & Folders** ######################################


**architecture.drawio.png** - This is presenting Architecture of conversational chat bot flow.

**conversation.py** - This file has bedrock connection and langchin code for prompt and response. We are configuring Bedrock for handling the prompt with sync documents and store embeeding vector in DB.





################################ **AWS SERVICES** ############################################


We are using server less architecture for creating this conversational AI bot. Which will help as to focus on code only and we 
do not need maintaning the configuration.

**We are using Following services** - 
1. **AWS CloudFront**
2. **Lambda**
3. **Secret Manager**
4. **Aurora PostgreSQL**
5. **AWS Bedrock**
6. **AWS S3 Bucket**
7. **Embedding & LLM Models**
8. **API Gateway**
9. **Notification**


**S3 UI bucket** - This bucket will use for UI code upload and map with CloudFront for render in URL.

**S3 document-raw bucket** - When we will upload document from UI than document will upload in this bucket and it will trigger event.

**AWS CloudFront** - CloudFront we are using for UI handle and render that from URL mapping. for now I am using streamlit for local and later we will deploy that and maintain in cloudFront.


##################### **Lambda's** #########################

There are multiple lambda we are using for code handling for conversational AI bot.

+ 1. **chat-bot** - (**conversation.py**) This lambda handle conversational code with documents and it will configure bedrock knowledge base RAG configuration, which will help to retrieve response for particular prompt. 

+ 2. **document-sync** - (**docs_sync.py**) This lambda handle document sync code code, when document will upload in s3 bucket than event will trigger and it will call this lambda. After calling this lambda will sync all new document with the help of bedrock knowledge base and KB will store all embedding in postgreSQl db.


**Secret Manager** - Secret manager will store DB credential and we can fetch this for retrive data. Basically this secret needs for bedrock, when bedrcok will configure than we need to pass this secrets ARN for access read & write data in vector DB for embedding store.


**Aurora PostgreSQL** - We are using aurora postgresql db for serverless and we do not use any extra configuration. This DB will store vector embedding and meta data as well.


**NOtification** - S3 notification we will enable that when document upload than we will trigger that and this will call document-sync lambda for document syncing.


**API Gateway** - API gateway we will use for creating api, here we will using Restfull API for interacting with UI specially for conversation and store data.

############# **API ENDPOINTS** ##########

+ **/chat/conversation** - This endpoint conncet with Knowledge Base, when user ask any prompt than this API will call and it will send request to bedrock knowledge base with all payload and RAG configurtion, It will connect and retrieve information from vector embedding and send to user.





################# **AWS BEDROCK** #####################

Bedrock help to create AI projeect with RAG, chatbot, agent.
We are using Amazon Bedrock to solve this problem and get response.

**Bedrock-Knowledge Base** - THis is Bedrock component which will help to create RAG functionality. We need to configure other componant for all setup like - vector database, datasource, embedding model.


########### **Bedrock SETUP** #############

**S3 bucket** - This is data source of all documents storage. It will store documents like - pdf, docx, text file.

**Vector Database** - We choose vector database which will store vector embedding , here I am choosing **AURORA POSTGRESQL**.
                    this is relational database and manage vectors well as columns and its not so costly as well.
                    + Database - conversdation-AI
                    + Table - bedrock_embedding
                    + Fields - Id, chunks, embedding, custome_field

**Embedding Model** - here we can select any model for embedding like - titel, nova, cohere. for now I am working with 
                      **Cohere V3**. here this will use **RecursiveTextEmbedding**.

**Chunking** - Chunking is defferent tyeps we have  but as per we are working on text so selecting **Sementic Chunking**
               which will devide chunks in 512 tokens for each.







