from fastapi import UploadFile,File,HTTPException
import os
import uuid
import shutil
from src.loaders.pdf_loader import load_pdf
#save file
UPLOAD_DIR = "uploads"
# ✅ Ensure directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_file(file):
    fileid=str(uuid.uuid4())
    filename=f"{fileid}.pdf"
    file_path=os.path.join(UPLOAD_DIR,filename)

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    documents = load_pdf(file_path)
    
    return{
        "file_id":fileid,
        "filename":filename,
        "path":file_path
    }