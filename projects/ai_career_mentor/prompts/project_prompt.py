from langchain_core.prompts import PromptTemplate


project_prompt = PromptTemplate(
    template="""
You are an AI career mentor.

Based on the user's career analysis and personalized roadmap,
recommend practical projects that will help the user become
job-ready for their target role.

Career Analysis:
{career_analysis}

Roadmap:
{roadmap}

Recommend 3 projects.

For each project provide:
- A clear project title
- Difficulty level
- Purpose of the project
- Technology stack
- Key features

The projects should:
1. Match the user's target role.
2. Help improve the user's missing skills.
3. Progress from easier to more advanced.
4. Be realistic for a beginner/intermediate developer.
5. Be strong enough to demonstrate on GitHub.
""",
    input_variables=["career_analysis", "roadmap"]
)