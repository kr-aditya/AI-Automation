import os
import tempfile

import streamlit as st

from utils.resume_pipeline import build_resume_vector_store
from chains.resume_analysis_chain import (
    resume_analysis_chain,
    format_resume_docs,
)
from chains.career_chain import career_chain
from chains.roadmap_chain import roadmap_chain
from chains.project_chain import project_chain
from chains.interview_chain import interview_chain


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🤖",
    layout="wide",
)


# ============================================================
# FUNCTIONS
# ============================================================

def analyze_resume(uploaded_file):
    """
    Run the complete Career Mentor pipeline
    using the uploaded resume.
    """

    # --------------------------------------------------------
    # 1. Save uploaded resume temporarily
    # --------------------------------------------------------

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf",
    ) as temp_file:

        temp_file.write(uploaded_file.getbuffer())
        resume_path = temp_file.name

    try:

        # ----------------------------------------------------
        # 2. Build Resume Vector Store
        # ----------------------------------------------------

        vector_store = build_resume_vector_store(
            resume_path
        )

        # ----------------------------------------------------
        # 3. Retrieve relevant resume information
        # ----------------------------------------------------

        query = """
        candidate technical skills experience projects education
        professional background career profile
        """

        documents = vector_store.similarity_search(
            query,
            k=6,
        )

        # ----------------------------------------------------
        # 4. Format retrieved documents
        # ----------------------------------------------------

        context = format_resume_docs(documents)

        # ----------------------------------------------------
        # 5. Resume Analysis
        # ----------------------------------------------------

        resume_result = resume_analysis_chain.invoke({
            "context": context
        })

        # ----------------------------------------------------
        # 6. Career Analysis
        # ----------------------------------------------------

        career_result = career_chain.invoke({
            "context": resume_result.model_dump_json(
                indent=2
            )
        })

        # ----------------------------------------------------
        # 7. Career Roadmap
        # ----------------------------------------------------

        roadmap_result = roadmap_chain.invoke({
            "career_analysis": career_result.model_dump_json(
                indent=2
            )
        })

        # ----------------------------------------------------
        # 8. Project Recommendations
        # ----------------------------------------------------

        project_result = project_chain.invoke({
            "career_analysis": career_result.model_dump_json(
                indent=2
            ),
            "roadmap": roadmap_result.model_dump_json(
                indent=2
            ),
        })

        # ----------------------------------------------------
        # 9. Interview Preparation
        # ----------------------------------------------------

        interview_result = interview_chain.invoke({
            "career_analysis": career_result.model_dump_json(
                indent=2
            ),
            "roadmap": roadmap_result.model_dump_json(
                indent=2
            ),
            "projects": project_result.model_dump_json(
                indent=2
            ),
        })

        return (
            resume_result,
            career_result,
            roadmap_result,
            project_result,
            interview_result,
        )

    finally:

        # Remove temporary uploaded file
        if os.path.exists(resume_path):
            os.remove(resume_path)


# ============================================================
# UI
# ============================================================

st.title("🤖 AI Career Mentor")

st.write(
    "Upload your resume and get a personalized career analysis, "
    "learning roadmap, project recommendations, and interview preparation."
)


uploaded_file = st.file_uploader(
    "📄 Upload your resume",
    type=["pdf"],
)


if uploaded_file:

    st.success(
        f"Resume uploaded: {uploaded_file.name}"
    )

    if st.button(
        "🚀 Analyze My Career",
        type="primary",
    ):

        with st.spinner(
            "Analyzing your resume and building your career plan..."
        ):

            try:

                (
                    resume_result,
                    career_result,
                    roadmap_result,
                    project_result,
                    interview_result,
                ) = analyze_resume(uploaded_file)

                st.success(
                    "Career analysis completed successfully!"
                )

                # ==================================================
                # CAREER ANALYSIS
                # ==================================================

                st.header("📊 Career Analysis")

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Current Level")
                    st.write(
                        career_result.current_level
                    )

                with col2:
                    st.subheader("Job-Readiness Score")
                    st.metric(
                        "Match Score",
                        f"{career_result.match_score}/100",
                    )

                st.subheader("💪 Strengths")

                for strength in career_result.strengths:
                    st.write(f"• {strength}")

                st.subheader("⚠️ Weaknesses")

                for weakness in career_result.weaknesses:
                    st.write(f"• {weakness}")

                st.subheader("📚 Missing Skills")

                for skill in career_result.missing_skills:
                    st.write(f"• {skill}")

                st.subheader("🎯 Learning Priority")

                for priority in career_result.learning_priority:
                    st.write(f"• {priority}")

                st.subheader("📝 Career Summary")

                st.write(
                    career_result.career_summary
                )

                # ==================================================
                # ROADMAP
                # ==================================================

                st.divider()

                st.header("🗺️ Personalized Career Roadmap")

                st.json(
                    roadmap_result.model_dump()
                )

                # ==================================================
                # PROJECTS
                # ==================================================

                st.divider()

                st.header("🚀 Recommended Projects")

                st.json(
                    project_result.model_dump()
                )

                # ==================================================
                # INTERVIEW
                # ==================================================

                st.divider()

                st.header("🎤 Interview Preparation")

                st.json(
                    interview_result.model_dump()
                )

            except Exception as error:

                st.error(
                    "Something went wrong while analyzing the resume."
                )

                st.exception(error)