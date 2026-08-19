from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

from schemas.resume_analysis import ResumeAnalysis
from utils.llm import llm


# ------------------------------------------------------------
# 1. FORMAT RETRIEVED RESUME DOCUMENTS
# ------------------------------------------------------------

def format_resume_docs(documents: list[Document]) -> str:
    """
    Convert retrieved LangChain Documents
    into plain text for the LLM.
    """

    parts = []

    for i, document in enumerate(documents, start=1):
        parts.append(
            f"[Resume Section {i}]\n"
            f"{document.page_content}"
        )

    return "\n\n".join(parts)


# ------------------------------------------------------------
# 2. PROMPT
# ------------------------------------------------------------

resume_analysis_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert AI Career Mentor.

Analyze the candidate using ONLY the information provided
in the resume context.

Do NOT invent:
- skills
- experience
- projects
- education
- certifications
- achievements

Analyze the candidate's:

1. Professional summary
2. Current or recent role
3. Suitable job roles
4. Technical skills
5. Strengths
6. Skill gaps
7. Recommended projects

If information is not present in the resume,
do not assume it.

RESUME CONTEXT:
----------------
{context}
----------------
"""
    ),
    (
        "human",
        "Analyze this candidate's resume."
    )
])


# ------------------------------------------------------------
# 3. STRUCTURED LLM
# ------------------------------------------------------------

analysis_llm = llm.with_structured_output(ResumeAnalysis)


# ------------------------------------------------------------
# 4. CAREER ANALYSIS CHAIN
# ------------------------------------------------------------

resume_analysis_chain = (
    resume_analysis_prompt
    | analysis_llm
)