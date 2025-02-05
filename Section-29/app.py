import streamlit as st
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("human", "Question:{question}")
    ]
)

def generate_response(question, llm, temperature):
    llm=ChatOllama(model=llm, temperature=temperature)
    output_parser = StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

st.title("Enhanced Chatbot with Ollama")
st.sidebar.title("Settings")
selectLLM = st.sidebar.selectbox("Select an Ollama model", ["deepseek-r1:8b", "llama3.2"])
temperature=st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)

st.write("Please ask a question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input, selectLLM, temperature)
    st.write(response)
else:
    st.write("Please enter a question")





