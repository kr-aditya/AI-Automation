def format_documents(documents) -> str:
    return "\n\n".join(
        f"Source: {doc.metadata.get('source')}\n"
        f"Video ID: {doc.metadata.get('video_id')}\n"
        f"{doc.page_content}"
        for doc in documents
    )