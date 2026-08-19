import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from schemas.career_schema import CareerAnalysis
from utils.llm import llm


load_dotenv()


# ============================================================
# LLM
# ============================================================

llm = llm


# ============================================================
# STRUCTURED OUTPUT
# ============================================================

career_llm = llm.with_structured_output(CareerAnalysis)


# ============================================================
# CAREER ANALYSIS PROMPT
# ============================================================

career_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI Career Mentor.

Analyze the candidate using ONLY the information provided
in the resume context.

Do NOT invent:
- experience
- skills
- projects
- education
- achievements
- job history

If something is not present in the resume, do not assume it.

Your task is to evaluate the candidate's current career position,
job readiness, strengths, weaknesses, missing skills, and learning
priorities.

Be realistic and practical.

Return the answer strictly according to the CareerAnalysis
structured schema.
"""
    ),
    (
        "human",
        """
RESUME CONTEXT:

{context}
"""
    )
])


# ============================================================
# CAREER ANALYSIS CHAIN
# ============================================================

career_chain = career_prompt | career_llm