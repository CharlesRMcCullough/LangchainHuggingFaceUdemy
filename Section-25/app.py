from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st


## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. Please repoonse to the question asked. If you don't say you don't know.",
        ),
        ("user", "Question:{question}"),
    ]
)

## Streamwork framework
st.title("Langchain Demo with Llama3.2")
input_text = st.text_input("Please ask a question")

## Call Llama model

llm = Ollama(model="llama3.2:latest")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
