from langchain_core.documents import Document


def create_document(transcript: str, video_id: str) -> Document:
    return Document(
        page_content=transcript,
        metadata={
            "source": "youtube",
            "video_id": video_id,
        },
    )