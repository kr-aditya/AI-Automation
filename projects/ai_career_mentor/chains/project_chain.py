from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.project_prompt import project_prompt
from schemas.project_schema import ProjectSchema
from utils.llm import llm

load_dotenv()





structured_model = llm.with_structured_output(
    ProjectSchema
)


project_chain = (
    project_prompt
    | structured_model
)