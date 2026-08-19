from utils.resume_loader import load_resume
from utils.resume_splitter import split_resume
from utils.embeddings import create_embedding_model
from utils.vector_store import create_vector_store


def build_resume_vector_store(file_path: str):

    print("\nLoading resume...")

    documents = load_resume(file_path)

    print(f"Loaded {len(documents)} pages.")

    print("Splitting resume...")

    chunks = split_resume(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating embeddings...")

    embedding_model = create_embedding_model()

    print("Creating Chroma vector store...")

    vector_store = create_vector_store(
        chunks,
        embedding_model,
    )

    print("Resume vector store ready.")

    return vector_store