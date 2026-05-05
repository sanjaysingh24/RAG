from fastapi import UploadFile,APIRouter,File,HTTPException
from src.service.pdf_service import save_file

uploadrouter=APIRouter(prefix="/api",tags=["upload"])


@uploadrouter.post("/upload")
async def upload_file(file:UploadFile=File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400,detail="Only PDF file allowed")
    
    file_data = await save_file(file)
    return {
        "message":"File uploaded Successfully",
        "data":file_data
    }