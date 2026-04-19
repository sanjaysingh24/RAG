from fastapi import APIRouter
from src.schema.chat_schema import ChatRequest
from src.service.rag_service import mychat
from fastapi import UploadFile,File,HTTPException
from src.service.pdf_service import save_file
from src.vectordb.vectordb import get_retriver

ragrouter = APIRouter(prefix="/api",tags=["rag"])

@ragrouter.post("/chat")
def ask_agent(data:ChatRequest):
    retriever = get_retriver() 

    
    
    ai_response = mychat(data.message, retriever)

    return {
        "question": data.message,
        "answer": ai_response
    }

