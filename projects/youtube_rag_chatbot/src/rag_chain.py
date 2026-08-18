from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from sources import format_sources


def format_docs(documents):
    return "\n\n".join(
        f"Source: {doc.metadata.get('source')}\n"
        f"Video ID: {doc.metadata.get('video_id')}\n"
        f"{doc.page_content}"
        for doc in documents
    )


def create_rag_chain(retriever, prompt, llm):

    retrieve_documents = (
        itemgetter("question")
        | retriever
    )

    rag_chain = (
        RunnablePassthrough.assign(
            documents=retrieve_documents
        )
        .assign(
            context=(
                itemgetter("documents")
                | RunnableLambda(format_docs)
            )
        )
        .assign(
            answer=(
                {
                    "context": itemgetter("context"),
                    "question": itemgetter("question"),
                }
                | prompt
                | llm
                | StrOutputParser()
            )
        )
        | RunnableLambda(
            lambda data: {
                "answer": data["answer"],
                "sources": format_sources(data["documents"]),
            }
        )
    )

    return rag_chain