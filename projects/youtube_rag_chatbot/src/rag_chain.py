from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough


def create_rag_chain(retriever, prompt, llm):

    def format_docs(documents):
        return "\n\n".join(
            f"Source: {doc.metadata.get('source')}\n"
            f"Video ID: {doc.metadata.get('video_id')}\n"
            f"{doc.page_content}"
            for doc in documents
        )

    rag_chain = (
        RunnablePassthrough.assign(
            context=(
                itemgetter("question")
                | retriever
                | RunnableLambda(format_docs)
            )
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain