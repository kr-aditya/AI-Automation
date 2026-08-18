from transcript import get_transcript
from documents import create_document
from splitter import split_document
from embeddings import create_embedding_model
from vector_store import create_vector_store
from retrieval import create_retriever


video_id = "Oa0ZHfcalCM"

# 1. Load transcript
transcript = get_transcript(video_id)

# 2. Create document
document = create_document(
    transcript,
    video_id,
)

# 3. Split
chunks = split_document(document)

# 4. Embeddings
embedding_model = create_embedding_model()

# 5. Vector store
vector_store = create_vector_store(
    chunks,
    embedding_model,
)

# 6. Retriever
retriever = create_retriever(
    vector_store,
    k=3,
)

# 7. Search
question = "What is AI"

results = retriever.invoke(question)

print(f"Retrieved {len(results)} documents.")

for index, document in enumerate(results, start=1):
    print("\n" + "=" * 60)
    print(f"RESULT {index}")
    print("=" * 60)

    print(document.page_content[:500])
    print("\nMetadata:", document.metadata)