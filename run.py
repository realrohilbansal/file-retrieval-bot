import streamlit as st
from langchain.llms.openai import OpenAI
import os
import enquiry
# from io import StringIO

openai_api_key = "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"
os.environ["OPENAI_API_KEY"] = openai_api_key

llm = OpenAI(temperature=0.8)

# file = './Dataset.txt'

def chatbot(llm, file, question):
    chunks = enquiry.chunking(file)
    vectordb = enquiry.embedder(chunks)
    response = enquiry.query(vectordb, llm, question)
    return response

st.title("College Enquiry Bot")
st.header("Welcome to the College Enquiry Bot")
st.subheader("Please enter your query below")

question = st.text_input("Enter your question here")

if question:
    response = chatbot(llm, file, question)
    while response is None:
        st.text("Response is being generated...")
    st.subheader("Response: ")
    st.write(response)