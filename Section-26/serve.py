import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)

# Create prompt template
generic_template = "Translate the following into {language}"

prompt = ChatPromptTemplate([("system", generic_template), ("user", "{text}")])

parser = StrOutputParser()

chain = prompt | model | parser


# App definition

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using Langchain runnable interface",
)

add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# make sure to add /docs to get swagger UI
