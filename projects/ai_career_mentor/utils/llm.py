import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model=os.getenv("MODEL"),
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)