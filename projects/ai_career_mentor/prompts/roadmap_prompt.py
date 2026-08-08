from langchain_core.prompts import ChatPromptTemplate


roadmap_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert AI career mentor.

Create a practical and realistic learning roadmap
for the user's target career.

Use the career analysis provided below.

Career Analysis:
{career_analysis}

The roadmap should:
- Be suitable for the user's current skill level.
- Prioritize the most important skills.
- Progress from fundamentals to advanced topics.
- Include practical projects.
- Avoid unnecessary technologies.
- Be realistic for a beginner.
"""
    ),
    (
        "human",
        "Create a personalized learning roadmap for me."
    )
])