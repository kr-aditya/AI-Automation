import streamlit as st


st.set_page_config(
    page_title="YouTube RAG Chatbot",
    page_icon="🎥",
    layout="centered",
)


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
        st.info(
            "Video processing will be connected here."
        )


# --------------------------------------------------
# QUESTION
# --------------------------------------------------

question = st.text_input(
    "Ask a question",
    placeholder="What is this video about?",
)


if st.button("Ask"):

    if not question:
        st.warning("Please enter a question.")

    else:
        st.info(
            "RAG question answering will be connected here."
        )