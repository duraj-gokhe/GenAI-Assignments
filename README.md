**CONVERSATIONAL AI BOT**

Conversational AI bot for own documents with RAG and Embedding vector
<br><br>

################################  **Files & Folders**  ######################################
<br>

**architecture.drawio.png** - This is presenting Architecture of conversational chat bot flow.

**conversation.py** - This file has bedrock connection and langchin code for prompt and response. We are configuring Bedrock for handling the prompt with sync documents and store embeeding vector in DB.

**chat_bot_ui.py** - This file present UI code which has small code for prompt text box and submit button to call API.

**requirements.txt** - This file has all installation package which we need to require to run this code.


<br><br>


################################  **Application WorkFlow** #####################################

<br>

**Requirements** ---

+ pip install python
+ install requirements.txt file

**Applcatiion Flow** --- 
<br>
This application I run in AWS but URL is not live and locally I have setup all things.

+ User can upload documents from upload files(5 files allow in one time)
+ This upload file functionality will call **/document/upload_doc** end point and uplaod document in **S3 DataSource bucket**
+ When file upload come form UI, It will be in dictionary format which has filename as key and encoding format of file content as value.
+ After that that API will take and convert in decoding format and upload in s3 bucket.
+ After uploading file in S3 bucket , bucket will trigger event than it will call **document-sync lambda**
+ Document sync lambda will run and call to **Start_injetion_job** for inject document with bedrock knowledgebase.
+ Bedrock Knowledge base split documents in chunks and store **embedding** in **postgreSQL** db in vector table.
+ After syncing completion user can ask prompt related to that document.
+ When user will ask prompt than **chat/conversation** API endpoint will call and it will call **RAG** or **bedrock API** for response.
+ After bedrock API call RAG will check all prompt validation and parameter for RAG and get response accordingly.
+ After getting response user will get citation part also with response , which will give document reference for user to check
which document it is refereing and  giving response.


<br><br>

################################  **AWS SERVICES**  ############################################

<br>
We are using server less architecture for creating this conversational AI bot. Which will help as to focus on code only and we 
do not need maintaning the configuration.
<br>

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
<br><br>

**S3 UI bucket** - This bucket will use for UI code upload and map with CloudFront for render in URL.

**S3 document-raw bucket** - When we will upload document from UI than document will upload in this bucket and it will trigger event.

**AWS CloudFront** - CloudFront we are using for UI handle and render that from URL mapping. for now I am using streamlit for local and later we will deploy that and maintain in cloudFront.

**Lambda** - There are multiple lambda we are using for code handling for conversational AI bot.

- **chat-bot** - (**conversation.py**) This lambda handle conversational code with documents and it will configure bedrock knowledge base RAG configuration, which will help to retrieve response for particular prompt. 

- **document-sync** - (**docs_sync.py**) This lambda handle document sync code code, when document will upload in s3 bucket than event will trigger and it will call this lambda. After calling this lambda will sync all new document with the help of bedrock knowledge base and KB will store all embedding in postgreSQl db.

<br>

**Secret Manager** - Secret manager will store DB credential and we can fetch this for retrive data. Basically this secret needs for bedrock, when bedrcok will configure than we need to pass this secrets ARN for access read & write data in vector DB for embedding store.

<br>

**Aurora PostgreSQL** - We are using aurora postgresql db for serverless and we do not use any extra configuration. This DB will store vector embedding and meta data as well.

<br>

**NOtification** - S3 notification we will enable that when document upload than we will trigger that and this will call document-sync lambda for document syncing.

<br>

 **API Gateway** - API gateway we will use for creating api, here we will using Restfull API for interacting with UI specially for conversation and store data.

- **API ENDPOINTS**

    1.  **/chat/conversation** - This endpoint conncet with Knowledge Base, when user ask any prompt than this API will call and it will send request to bedrock knowledge base with all payload and RAG configurtion, It will connect and retrieve information from vector embedding and send to user.

<br>

**AWS BEDROCK** - Bedrock help to create AI projeect with RAG, chatbot, agent. We are using Amazon Bedrock to solve this problem and get response.

+ **Bedrock-Knowledge Base** - THis is Bedrock component which will help to create RAG functionality. We need to configure other componant for all setup like - vector database, datasource, embedding model.

+ **Bedrock SETUP**

    - **S3 bucket** - This is data source of all documents storage. It will store documents like - pdf, docx, text file.

    - **Vector Database** - We choose vector database which will store vector embedding , here I am choosing **AURORA POSTGRESQL**.This is relational database and manage vectors well as columns.
        + Database - conversdation-AI
        + Table - bedrock_embedding
        + Fields - Id, chunks, embedding, custome_field

    - **Embedding Model** - here we can select any model for embedding like - titel, nova, cohere. for now I am working with **Cohere V3**. here this will use **RecursiveTextEmbedding**.

    - **Chunking** - Chunking is defferent tyeps we have  but as per we are working on text so selecting **Sementic  Chunking** which will devide chunks in 512 tokens for each.

<br>

############################## **Feature Enhancement** ##############################

<br><br>

+ We can manage role based document manage.
+ We can enhance the feature of multiple teams and manage documents.
+ Enhance the CI/CD pipeline 
+ We can enhance the security for authentication.
+ We can enhance the other task like - resume format, other APIs
+ We can enhance the multiple agent with the help of Bedrock.






