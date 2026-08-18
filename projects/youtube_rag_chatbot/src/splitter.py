from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_document(document):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    )

    return splitter.split_documents([document])