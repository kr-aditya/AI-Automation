from chains.career_chain import career_chain


resume_analysis = """
Candidate Summary:
Computer Science/MCA candidate focused on AI automation and GenAI.

Current Role:
Entry-level / fresher.

Suitable Roles:
AI Automation Engineer
GenAI Engineer
Python Developer

Technical Skills:
Python
LangChain
RAG
FastAPI
React
JavaScript

Strengths:
Python fundamentals
Frontend development
LLM application development
RAG implementation

Skill Gaps:
Agents
Advanced LangChain
Production deployment
Docker
Cloud

Recommended Projects:
AI Career Mentor
RAG Document Assistant
AI Automation Platform
"""


result = career_chain.invoke({
    "resume_analysis": resume_analysis
})


print("=" * 60)
print("CAREER ANALYSIS")
print("=" * 60)

print("\nCURRENT LEVEL:")
print(result.current_level)

print("\nMATCH SCORE:")
print(result.match_score)

print("\nSTRENGTHS:")
for item in result.strengths:
    print("-", item)

print("\nWEAKNESSES:")
for item in result.weaknesses:
    print("-", item)

print("\nMISSING SKILLS:")
for item in result.missing_skills:
    print("-", item)

print("\nLEARNING PRIORITY:")
for item in result.learning_priority:
    print("-", item)

print("\nCAREER SUMMARY:")
print(result.career_summary)