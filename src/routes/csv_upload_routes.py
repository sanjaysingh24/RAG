from fastapi import APIRouter,UploadFile,File,HTTPException
from src.service.csv_service import save_csvfile

csvrouter = APIRouter(prefix="/api",tags=["csv_upload"])

@uploadrouter.post("/upload_csv")
async def upload_csv(file:UploadFile=File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400,detail="Only CSV file allowed")
    file_data = await save_csvfile(file)
    return {
        "status":True,
        "message":"CSV File uploaded Successfully",
        
    }