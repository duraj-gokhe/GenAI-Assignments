import streamlit as st
from Test import *


st.header("Research Tool")
user_input = st.text_input("Enter Prompt")

if st.button("Summarize"):
    result = models_calling(user_input)
    st.write(result.get("Output"))

