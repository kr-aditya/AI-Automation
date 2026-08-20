# YouTube RAG Chatbot

A Retrieval-Augmented Generation (RAG) application for asking questions about YouTube video content. The application processes a video's transcript, creates searchable embeddings, retrieves relevant transcript sections, and uses an LLM to generate answers grounded in the retrieved context.

## Features

- YouTube video input
- Transcript extraction and processing
- Text chunking for retrieval
- Embedding generation
- Vector similarity search
- Retrieval-Augmented Generation (RAG)
- Groq-powered LLM responses
- Streamlit web interface
- Modular RAG architecture
- Local vector-store support

## Architecture

```text
YouTube URL
    |
    v
Video ID Extraction
    |
    v
Transcript Retrieval
    |
    v
Text Splitting
    |
    v
Embeddings
    |
    v
Vector Store
    |
    v
Similarity Retrieval
    |
    v
Relevant Context
    |
    v
RAG Prompt + LLM
    |
    v
Grounded Answer
    |
    v
Streamlit UI
```

## Project Structure

```text
youtube_rag_chatbot/
|
+-- app/
|   +-- streamlit_app.py       # Streamlit interface
|
+-- src/
|   +-- llm.py                 # LLM configuration
|   +-- pipeline.py            # End-to-end RAG pipeline
|   +-- prompts.py             # RAG prompts
|   +-- rag_chain.py           # Retrieval + generation chain
|   +-- rag.py                 # RAG orchestration
|   +-- retrieval.py           # Relevant document retrieval
|   +-- sources.py             # Source/transcript handling
|   +-- splitter.py            # Text chunking
|   +-- transcript.py          # Transcript processing
|   +-- vector_store.py        # Vector-store operations
|   +-- youtube.py             # YouTube handling
|
+-- data/                      # Local application data/cache
+-- .env.example               # Environment variable template
+-- .gitignore
+-- pyproject.toml             # Python package configuration
+-- requirements.txt           # Dependencies
+-- README.md
```

## How the RAG Pipeline Works

1. The user provides a YouTube video.
2. The application extracts the video information.
3. The transcript is retrieved and processed.
4. The transcript is split into smaller chunks.
5. Chunks are converted into embeddings.
6. Embeddings are stored in a vector store.
7. The user's question is used to retrieve semantically relevant chunks.
8. Retrieved context is passed to the LLM.
9. The LLM generates an answer using the retrieved context.

The important idea is that the LLM does not have to rely only on its general knowledge. Relevant information is retrieved from the video's transcript and supplied as context.

## Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB / vector store
- Hugging Face embeddings
- Groq
- YouTube transcript/video tooling
- Git & GitHub

## Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd youtube_rag_chatbot
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create `.env` from `.env.example` and add:

```env
GROQ_API_KEY=your_api_key_here
```

Never commit `.env` or API keys to GitHub.

### 5. Start the application

From the project root:

```bash
streamlit run app/streamlit_app.py
```

## Security

API keys are loaded through environment variables. Secrets should never be hard-coded or committed to the repository.

## Why This Project Is Portfolio-Worthy

This project demonstrates practical GenAI engineering concepts beyond simply calling an LLM API:

- RAG architecture
- Embeddings and semantic search
- Vector databases
- Document/transcript processing
- Prompt engineering
- LLM integration
- Modular Python architecture
- Streamlit application development
- Environment and dependency management

## Future Improvements

- Streaming responses
- Source/chunk citations
- Retrieval score display
- Conversation memory
- Multiple-video knowledge bases
- Transcript caching
- Better transcript/error handling
- Automated RAG evaluation
- Docker deployment
- Cloud deployment

## Portfolio Focus

Development-only test scripts and unnecessary entry-point files are intentionally excluded from the portfolio-facing repository. The repository focuses on the application and core RAG implementation.

Built as a hands-on GenAI / RAG engineering project.
