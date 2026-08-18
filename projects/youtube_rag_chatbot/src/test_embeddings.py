from transcript import get_transcript
from documents import create_document
from splitter import split_document
from embeddings import create_embedding_model
from vector_store import create_vector_store


video_id = "Oa0ZHfcalCM"

# 1. Get transcript
transcript = get_transcript(video_id)

# 2. Create LangChain Document
document = create_document(
    transcript,
    video_id,
)

# 3. Split into chunks
chunks = split_document(document)

print(f"Created {len(chunks)} chunks.")

# 4. Create embedding model
embedding_model = create_embedding_model()

print("Embedding model loaded.")

# 5. Create FAISS vector store
vector_store = create_vector_store(
    chunks,
    embedding_model,
)

print("FAISS vector store created.")

query = "What is RAG?"

results = vector_store.similarity_search(
    query,
    k=3,
)

print("\nSearch Results:")
print("=" * 60)

for index, result in enumerate(results, start=1):
    print(f"\nResult {index}")
    print(result.page_content[:500])
    print("Metadata:", result.metadata)