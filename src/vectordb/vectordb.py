import os
from dotenv import load_dotenv
load_dotenv()
from langchain_pinecone import PineconeVectorStore
from src.config.embeddings import embeddings

def store_in_pinecoce(chunks):
    try:

        vector_store=PineconeVectorStore.from_documents(
            documents=chunks,
            embedding=embeddings,
            index_name=os.getenv("PINECONE_INDEX_NAME")
        )
        return {
            "status":True
        }
    except Exception as e:
        return {
            "status":False
        }

def get_vectorstore():
    vector_store =PineconeVectorStore(
        index_name=os.getenv("PINECONE_INDEX_NAME"),
        embedding=embeddings
    )
    return vector_store

def get_retriver():
    vectordb=get_vectorstore()

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    return retriever