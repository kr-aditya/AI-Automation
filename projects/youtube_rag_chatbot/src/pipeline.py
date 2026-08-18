from transcript import get_transcript
from documents import create_document
from splitter import split_document
from embeddings import create_embedding_model
from vector_store import create_vector_store
from retrieval import create_retriever
from prompts import create_rag_prompt
from llm import create_llm
from rag_chain import create_rag_chain


def build_video_pipeline(video_id: str):
    # 1. Get transcript
    transcript = get_transcript(video_id)

    # 2. Create LangChain document
    document = create_document(
        transcript,
        video_id,
    )

    # 3. Split document
    chunks = split_document(document)

    # 4. Create embedding model
    embedding_model = create_embedding_model()

    # 5. Create vector store
    vector_store = create_vector_store(
        chunks,
        embedding_model,
    )

    # 6. Create retriever
    retriever = create_retriever(
        vector_store,
        k=3,
    )

    # 7. Create prompt
    prompt = create_rag_prompt()

    # 8. Create LLM
    llm = create_llm()

    # 9. Create RAG chain
    rag_chain = create_rag_chain(
        retriever,
        prompt,
        llm,
    )

    return rag_chain