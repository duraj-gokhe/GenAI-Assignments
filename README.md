**CONVERSATIONAL AI BOT**

Conversational AI bot for own documents with RAG and Embedding vector

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




################# **AWS BEDROCK** #####################

Bedrock help to create AI projeect with RAG, chatbot, agent.
We are using Amazon Bedrock to solve this problem and get response.

**Bedrock-Knowledge Base** - THis is Bedrock component which will help to create RAG functionality. We need to configure other componant for all setup like - vector database, datasource, embedding model.

**SETUP** ------

**S3 bucket** - This is data source of all documents storage. It will store documents like - pdf, docx, text file.

**Vector Database** - We choose vector database which will store vector embedding , here I am choosing **POSTGRESQL**.
                    this is relational database and manage vectors well as columns and its not so costly as well.

**Embedding Model** - here we can select any model for embedding like - titel, nova, cohere. for now I am working with 
                      **Cohere V3**. here this will use **RecursiveTextEmbedding**.

**Chunking** - Chunking is defferent tyeps we have  but as per we are working on text so selecting **Sementic Chunking**
               which will devide chunks in 512 tokens for each.







