from fastapi import FastAPI
from src.routes.rag_routes import ragrouter
from src.routes.upload_routes import uploadrouter

app  = FastAPI()
app.include_router(ragrouter)
app.include_router(uploadrouter)
@app.get("/")
def main():
    return {"message": "Hello World!"}