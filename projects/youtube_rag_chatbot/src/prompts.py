from langchain_core.prompts import ChatPromptTemplate


def create_rag_prompt():
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a helpful YouTube video assistant.

Answer the user's question ONLY using the provided
transcript context.

If the context does not contain enough information to
answer the question, say:
"I don't have enough information in the transcript to answer that."

Do not invent information.

Context:
{context}
""",
            ),
            (
                "human",
                "{question}",
            ),
        ]
    )