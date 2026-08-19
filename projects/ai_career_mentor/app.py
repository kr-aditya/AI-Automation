from chains.career_chain import career_chain
from chains.roadmap_chain import roadmap_chain
from chains.project_chain import project_chain
from chains.interview_chain import interview_chain

from chains.resume_analysis_chain import (
    resume_analysis_chain,
    format_resume_docs,
)

from utils.resume_pipeline import build_resume_vector_store

from utils.display import (
    display_career_analysis,
    display_roadmap,
    display_projects,
    display_interview_preparation,
)


# ============================================================
# CONFIGURATION
# ============================================================

RESUME_PATH = "data/resumes/resume.pdf"


# ============================================================
# RESUME RAG
# ============================================================

def run_resume_analysis():
    """
    Load the resume, create/load its vector store,
    retrieve relevant resume information, and analyze it.
    """

    print("\nLoading resume...\n")

    # Build/load the resume vector store
    vector_store = build_resume_vector_store(RESUME_PATH)

    query = """
    candidate technical skills experience projects education
    professional background career profile
    """

    documents = vector_store.similarity_search(
    query,
    k=6
)

    print(f"Retrieved {len(documents)} resume chunks.\n")

    # Convert retrieved documents into text context
    context = format_resume_docs(documents)

    # Analyze the resume using the Resume Analysis Chain
    resume_result = resume_analysis_chain.invoke({
        "context": context
    })

    return resume_result


# ============================================================
# CAREER ANALYSIS
# ============================================================

def run_career_analysis_from_resume(resume_result):
    """
    Use the structured resume analysis as input
    to the main Career Analysis chain.
    """

    resume_analysis = resume_result.model_dump_json(
        indent=2
    )

    return career_chain.invoke({
        "context": resume_analysis
    })


# ============================================================
# ROADMAP
# ============================================================

def run_roadmap(career_result):
    roadmap_input = {
        "career_analysis": career_result.model_dump_json(
            indent=2
        )
    }

    return roadmap_chain.invoke(roadmap_input)


# ============================================================
# PROJECT RECOMMENDATIONS
# ============================================================

def run_project_recommendations(
    career_result,
    roadmap_result,
):
    project_input = {
        "career_analysis": career_result.model_dump_json(
            indent=2
        ),
        "roadmap": roadmap_result.model_dump_json(
            indent=2
        ),
    }

    return project_chain.invoke(project_input)


# ============================================================
# INTERVIEW PREPARATION
# ============================================================

def run_interview_preparation(
    career_result,
    roadmap_result,
    project_result,
):
    interview_input = {
        "career_analysis": career_result.model_dump_json(
            indent=2
        ),
        "roadmap": roadmap_result.model_dump_json(
            indent=2
        ),
        "projects": project_result.model_dump_json(
            indent=2
        ),
    }

    return interview_chain.invoke(interview_input)


# ============================================================
# MAIN APPLICATION FLOW
# ============================================================

def main():

    print("=" * 65)
    print("🤖 AI Career Mentor")
    print("=" * 65)

    # ========================================================
    # 1. RESUME ANALYSIS
    # ========================================================

    resume_result = run_resume_analysis()

    # ========================================================
    # 2. CAREER ANALYSIS
    # ========================================================

    print("\nAnalyzing career profile...\n")

    career_result = run_career_analysis_from_resume(
        resume_result
    )

    display_career_analysis(career_result)

    # ========================================================
    # 3. ROADMAP
    # ========================================================

    print("\nGenerating personalized roadmap...\n")

    roadmap_result = run_roadmap(career_result)

    display_roadmap(roadmap_result)

    # ========================================================
    # 4. PROJECT RECOMMENDATIONS
    # ========================================================

    print("\nGenerating project recommendations...\n")

    project_result = run_project_recommendations(
        career_result,
        roadmap_result,
    )

    display_projects(project_result)

    # ========================================================
    # 5. INTERVIEW PREPARATION
    # ========================================================

    print("\nGenerating interview preparation...\n")

    interview_result = run_interview_preparation(
        career_result,
        roadmap_result,
        project_result,
    )

    display_interview_preparation(
        interview_result
    )

    # ========================================================
    # COMPLETE
    # ========================================================

    print("\n" + "=" * 65)
    print("🤖 CAREER MENTOR COMPLETE")
    print("=" * 65)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()