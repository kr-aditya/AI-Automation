from transcript import get_transcript
from documents import create_document
from splitter import split_document
from embeddings import create_embedding_model
from vector_store import create_vector_store
from retrieval import create_retriever
from prompts import create_rag_prompt
from llm import create_llm
from rag import create_rag_chain


video_id = "Oa0ZHfcalCM"


# -------------------------
# INDEXING
# -------------------------

transcript = get_transcript(video_id)

document = create_document(
    transcript,
    video_id,
)

chunks = split_document(document)

embedding_model = create_embedding_model()

vector_store = create_vector_store(
    chunks,
    embedding_model,
)


# -------------------------
# RETRIEVAL
# -------------------------

retriever = create_retriever(
    vector_store,
    k=3,
)


# -------------------------
# GENERATION
# -------------------------

prompt = create_rag_prompt()

llm = create_llm()

rag_chain = create_rag_chain(
    retriever,
    prompt,
    llm,
)


# -------------------------
# ASK QUESTION
# -------------------------

question = input("\nAsk a question about the video: ")

answer = rag_chain(question)

print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)
print(answer)