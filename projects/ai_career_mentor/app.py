from chains.career_chain import career_chain
from chains.roadmap_chain import roadmap_chain
from chains.project_chain import project_chain
from chains.interview_chain import interview_chain
from utils.display import (
    display_career_analysis,
    display_roadmap,
    display_projects,
    display_interview_preparation,
)


# ============================================================
# USER INPUT
# ============================================================

def get_user_profile():
    print("=" * 65)
    print("🤖 AI Career Mentor")
    print("=" * 65)

    name = input("Your Name: ")
    skills = input("Your Skills (comma separated): ")
    experience = input("Your Experience: ")
    target_role = input("Target Role: ")

    return {
        "name": name,
        "skills": skills,
        "experience": experience,
        "target_role": target_role,
    }


# ============================================================
# CAREER ANALYSIS
# ============================================================

def run_career_analysis(profile):
    return career_chain.invoke(profile)


# ============================================================
# ROADMAP
# ============================================================

def run_roadmap(career_result):
    roadmap_input = {
        "career_analysis": career_result.model_dump_json(indent=2)
    }

    return roadmap_chain.invoke(roadmap_input)


# ============================================================
# PROJECT RECOMMENDATIONS
# ============================================================

def run_project_recommendations(career_result, roadmap_result):
    project_input = {
        "career_analysis": career_result.model_dump_json(indent=2),
        "roadmap": roadmap_result.model_dump_json(indent=2),
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
        "career_analysis": career_result.model_dump_json(indent=2),
        "roadmap": roadmap_result.model_dump_json(indent=2),
        "projects": project_result.model_dump_json(indent=2),
    }

    return interview_chain.invoke(interview_input)


# ============================================================
# MAIN APPLICATION FLOW
# ============================================================

def main():
    profile = get_user_profile()

    print("\nAnalyzing profile...\n")

    # 1. Career Analysis
    career_result = run_career_analysis(profile)
    display_career_analysis(career_result)

    # 2. Roadmap
    roadmap_result = run_roadmap(career_result)
    display_roadmap(roadmap_result)

    # 3. Project Recommendations
    project_result = run_project_recommendations(
        career_result,
        roadmap_result,
    )
    display_projects(project_result)

    # 4. Interview Preparation
    interview_result = run_interview_preparation(
        career_result,
        roadmap_result,
        project_result,
    )
    display_interview_preparation(interview_result)

    print("\n" + "=" * 65)
    print("🤖 CAREER MENTOR COMPLETE")
    print("=" * 65)


if __name__ == "__main__":
    main()