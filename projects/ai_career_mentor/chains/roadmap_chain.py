from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.roadmap_prompt import roadmap_prompt
from schemas.roadmap_schema import RoadmapSchema
from utils.llm import llm

load_dotenv()





structured_model = llm.with_structured_output(
    RoadmapSchema
)


roadmap_chain = roadmap_prompt | structured_model

