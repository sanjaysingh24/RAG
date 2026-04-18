from pydantic import BaseModel

class ChatRequest(BaseModel):
    message:str

class UrlSchema(BaseModel):
    url:str