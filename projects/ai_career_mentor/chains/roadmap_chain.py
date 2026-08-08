from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.roadmap_prompt import roadmap_prompt
from schemas.roadmap_schema import RoadmapSchema


load_dotenv()


model = ChatGroq(
    model="llama-3.3-70b-versatile"
)


structured_model = model.with_structured_output(
    RoadmapSchema
)


roadmap_chain = roadmap_prompt | structured_model

