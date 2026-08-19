from langchain_chroma import Chroma


def create_vector_store(chunks, embedding_model):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./data/chroma_resume",
        collection_name="resume",
    )

    return vector_store