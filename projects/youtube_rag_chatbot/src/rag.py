from langchain_core.output_parsers import StrOutputParser


def create_rag_chain(retriever, prompt, llm):
    parser = StrOutputParser()

    def answer_question(question: str) -> str:
        documents = retriever.invoke(question)

        context = "\n\n".join(
            f"Source: {doc.metadata.get('source')}\n"
            f"Video ID: {doc.metadata.get('video_id')}\n"
            f"{doc.page_content}"
            for doc in documents
        )

        messages = prompt.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        response = llm.invoke(messages)

        return parser.invoke(response)

    return answer_question