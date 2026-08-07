from langchain_core.prompts import ChatPromptTemplate

career_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert AI Career Mentor.

Analyze the user's profile carefully.

Your task:
- Determine the candidate's current level.
- Give a realistic job readiness score.
- Identify strengths.
- Identify weaknesses.
- Identify missing skills.
- Suggest learning priorities.
- Write a short career summary.

{format_instructions}

Return ONLY the required structured output.
"""
    ),

    (
        "human",
        """
Candidate Profile

Name: {name}

Current Skills:
{skills}

Experience:
{experience}

Target Role:
{target_role}
"""
    )
])