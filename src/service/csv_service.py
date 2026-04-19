from fastapi import UploadFile,File,HTTPException
import os
import uuid
import shutil
from src.loaders.csv_loader import load_csv

#save file
UPLOAD_DIR="csv_uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)


async def save_csvfile(file):
    fileid = str(uuid.uuid4())
    filename=f"{fileid}.csv"
    file_path = os.path.join(UPLOAD_DIR,filename)

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    documents = load_csv(file_path)

    return {
        "file_id":fileid,
        "filename":filename,
        "path":file_path

    }