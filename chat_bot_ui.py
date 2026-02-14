import streamlit as st
from conversation import *


st.header("GenAI Conversation Assignment")
user_input = st.text_input("Enter Prompt")

if st.button("Submit"):
    result = conversation_kb(user_input)
    st.write(result.get("Response"))
    st.write(result.get("citation"))

