from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.project_prompt import project_prompt
from schemas.project_schema import ProjectSchema


load_dotenv()


model = ChatGroq(
    model="llama-3.3-70b-versatile"
)


structured_model = model.with_structured_output(
    ProjectSchema
)


project_chain = (
    project_prompt
    | structured_model
)