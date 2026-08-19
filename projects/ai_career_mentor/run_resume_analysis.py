from utils.resume_pipeline import build_resume_vector_store
from chains.resume_analysis_chain import (
    resume_analysis_chain,
    format_resume_docs
)


RESUME_PATH = "data/resumes/resume.pdf"


print("Loading resume...")


# ------------------------------------------------------------
# 1. Build/load resume vector store
# ------------------------------------------------------------

vector_store = build_resume_vector_store(RESUME_PATH)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)


# ------------------------------------------------------------
# 2. Retrieve relevant resume information
# ------------------------------------------------------------

query = """
candidate technical skills experience projects education
professional background career profile
"""

documents = retriever.invoke(query)


print(f"\nRetrieved {len(documents)} resume chunks.\n")


# ------------------------------------------------------------
# 3. Format retrieved documents
# ------------------------------------------------------------

context = format_resume_docs(documents)


# ------------------------------------------------------------
# 4. Run career analysis
# ------------------------------------------------------------

print("Analyzing resume...\n")

result = resume_analysis_chain.invoke({
    "context": context
})


# ------------------------------------------------------------
# 5. Display result
# ------------------------------------------------------------

print("=" * 60)
print("CAREER ANALYSIS")
print("=" * 60)

print("\nSUMMARY:")
print(result.candidate_summary)

print("\nCURRENT / RECENT ROLE:")
print(result.current_role)

print("\nSUITABLE ROLES:")
for role in result.suitable_roles:
    print(f"- {role}")

print("\nTECHNICAL SKILLS:")
for skill in result.technical_skills:
    print(f"- {skill}")

print("\nSTRENGTHS:")
for strength in result.strengths:
    print(f"- {strength}")

print("\nSKILL GAPS:")
for gap in result.skill_gaps:
    print(f"- {gap}")

print("\nRECOMMENDED PROJECTS:")
for project in result.recommended_projects:
    print(f"- {project}")