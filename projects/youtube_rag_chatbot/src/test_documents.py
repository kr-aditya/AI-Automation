from transcript import get_transcript
from documents import create_document
from splitter import split_document


video_id = "Oa0ZHfcalCM"

# 1. Get transcript
transcript = get_transcript(video_id)

print(f"Transcript characters: {len(transcript)}")

# 2. Convert transcript into a LangChain Document
document = create_document(
    transcript,
    video_id,
)

print(f"Document type: {type(document)}")
print(f"Metadata: {document.metadata}")

# 3. Split document into chunks
chunks = split_document(document)

print(f"Number of chunks: {len(chunks)}")

# 4. Inspect first chunk
print("\nFirst chunk:")
print(chunks[0].page_content)

print("\nFirst chunk metadata:")
print(chunks[0].metadata)