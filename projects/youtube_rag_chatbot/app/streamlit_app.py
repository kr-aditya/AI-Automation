import streamlit as st

from src.youtube import extract_video_id
from src.pipeline import build_video_pipeline


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="YouTube RAG Chatbot",
    page_icon="🎥",
    layout="centered",
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "video_id" not in st.session_state:
    st.session_state.video_id = None


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🎥 YouTube RAG Chatbot")

st.write(
    "Ask questions about a YouTube video using "
    "Retrieval-Augmented Generation."
)


# --------------------------------------------------
# VIDEO INPUT
# --------------------------------------------------

youtube_url = st.text_input(
    "YouTube Video URL",
    placeholder="Paste your YouTube URL here...",
)


if st.button("Process Video"):

    if not youtube_url:
        st.warning("Please enter a YouTube URL.")

    else:
        try:
            video_id = extract_video_id(youtube_url)

            with st.spinner(
                "Processing video... This may take a moment."
            ):
                rag_chain = build_video_pipeline(video_id)

            st.session_state.rag_chain = rag_chain
            st.session_state.video_id = video_id

            st.success("✅ Video processed successfully!")

        except Exception as error:
            st.error(
                f"Unable to process this video: {error}"
            )


# --------------------------------------------------
# SHOW PROCESSING STATUS
# --------------------------------------------------

if st.session_state.rag_chain is not None:

    st.info(
        f"Video ready: {st.session_state.video_id}"
    )


# --------------------------------------------------
# QUESTION
# --------------------------------------------------

question = st.text_input(
    "Ask a question",
    placeholder="What does this video explain?",
)


if st.button("Ask"):

    if st.session_state.rag_chain is None:
        st.warning(
            "Please process a YouTube video first."
        )

    elif not question:
        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner("Finding the answer..."):

            result = st.session_state.rag_chain.invoke(
                {
                    "question": question
                }
            )

        # ------------------------------
        # ANSWER
        # ------------------------------

        st.subheader("Answer")

        st.write(result["answer"])

        # ------------------------------
        # SOURCES
        # ------------------------------

        st.subheader("Sources")

        for source in result["sources"]:

            with st.expander(
                f"Source {source['index']}"
            ):

                st.write(
                    f"**Type:** {source['source']}"
                )

                st.write(
                    f"**Video ID:** {source['video_id']}"
                )

                st.write(
                    source["content"]
                )