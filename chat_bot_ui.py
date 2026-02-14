import streamlit as st


from io import StringIO
from conversation import *
from document_upload import *


st.header("GenAI Conversation Assignment")

try:

    ## File upload functionality 
    files = {}
    upload_file = st.file_uploader("Upload file", type=["pdf", "txt", "docx"])
    if upload_file is not None:
        file_name = upload_file.name
        
        # Read file as bytes
        bytes_data = upload_file.getvalue()

        # Decode the bytes to a string
        value = StringIO(bytes_data.decode("utf-8"))

        files[file_name] = files[value]

    response = document_upload(files)
    st.write(response)
    


    ## User query functionality and response
    user_input = st.text_input("Enter Prompt")

    if st.button("Submit"):
        result = conversation_kb(user_input)
        st.write(result.get("Response"))
        st.write(result.get("citation"))

except Exception as e:
    print(str(e))

