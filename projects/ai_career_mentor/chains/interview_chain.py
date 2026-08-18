from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.interview_prompt import interview_prompt
from schemas.interview_schema import InterviewSchema
from utils.llm import llm

load_dotenv()





structured_model = llm.with_structured_output(
    InterviewSchema
)


interview_chain = interview_prompt | structured_model


if __name__ == "__main__":

    career_analysis = """
    Target role: AI Automation Engineer

    Strengths:
    Python, JavaScript, React

    Missing skills:
    RAG, Vector Databases, FastAPI, Docker

    Weaknesses:
    Limited AI project experience
    """

    roadmap = """
    Phase 1: Python and backend fundamentals
    Phase 2: LangChain and LLM applications
    Phase 3: RAG and vector databases
    Phase 4: AI automation and deployment
    """

    projects = """
    1. AI Career Assistant
    2. RAG Document Assistant
    3. AI Automation Platform
    """

    result = interview_chain.invoke({
        "career_analysis": career_analysis,
        "roadmap": roadmap,
        "projects": projects
    })

    print(result)