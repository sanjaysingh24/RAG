from fastapi import FastAPI
from src.routes.rag_routes import ragrouter
from src.routes.upload_routes import uploadrouter
from src.routes.web_loader_route import webRouter
from src.routes.csv_upload_routes import csvrouter
app  = FastAPI()
app.include_router(ragrouter)
app.include_router(uploadrouter)
app.include_router(webRouter)
app.include_router(csvrouter)
@app.get("/")
def main():
    return {"message": "Hello World!"}