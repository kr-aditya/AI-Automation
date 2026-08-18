def format_sources(documents):
    sources = []

    for index, document in enumerate(documents, start=1):
        sources.append(
            {
                "index": index,
                "source": document.metadata.get("source"),
                "video_id": document.metadata.get("video_id"),
                "content": document.page_content,
            }
        )

    return sources