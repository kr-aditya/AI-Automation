from utils.resume_pipeline import build_resume_vector_store


RESUME_PATH = "data/resumes/resume.pdf"


vector_store = build_resume_vector_store(
    RESUME_PATH
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 4}
)

query = "What technical skills and projects does this candidate have?"

results = retriever.invoke(query)

print("\n" + "=" * 60)
print("RETRIEVED RESUME CONTENT")
print("=" * 60)

for i, document in enumerate(results, start=1):

    print(f"\n--- Result {i} ---")

    print(document.page_content)

    print("\nMetadata:")
    print(document.metadata)