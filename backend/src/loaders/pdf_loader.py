
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.vectordb.vectordb import store_in_pinecoce
from src.utils.deletefile import delete_file
from src.utils.textCleaner import clean_text
def load_pdf(file_path:str):
    try:
        loader = PyPDFLoader(file_path)
        docs=loader.load()
        for doc in docs:
            doc.page_content=clean_text(doc.page_content)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n\n","\n","."," ", ""]
        )
        chunks = splitter.split_documents(docs)
        vectordb = store_in_pinecoce(chunks)
        
       
        if vectordb["status"]==True:
            fdelete = delete_file(file_path)
            
      
    except Exception as e:

        return {
            "status":False
        }
    