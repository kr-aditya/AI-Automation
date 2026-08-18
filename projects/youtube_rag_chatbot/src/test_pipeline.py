from pipeline import build_video_pipeline


video_id = "Oa0ZHfcalCM"

rag_chain = build_video_pipeline(video_id)

question = input("\nAsk a question: ")

result = rag_chain.invoke(
    {
        "question": question
    }
)

print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)

print(result["answer"])

print("\n" + "=" * 60)
print("SOURCES")
print("=" * 60)

for source in result["sources"]:
    print(
        f"\nSource {source['index']}: "
        f"{source['content'][:300]}..."
    )