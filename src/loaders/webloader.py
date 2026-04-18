from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.vectordb.vectordb import store_in_pinecoce
from src.utils.textCleaner import clean_text
async def load_url(url:str):
    try:
        loader = WebBaseLoader(url)
        docs=loader.load()
        for doc in docs:
            doc.page_content= clean_text(doc.page_content)
        splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=100,
                separators=["\n\n","\n","."," ", ""]
        )
        chunks = splitter.split_documents(docs)
        vectordb = store_in_pinecoce(chunks)
    except Exception as a:
        print("Something error")