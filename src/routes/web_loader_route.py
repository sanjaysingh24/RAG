from fastapi import APIRouter
from src.schema.chat_schema import UrlSchema
from src.loaders.webloader import load_url
webRouter = APIRouter(prefix="/webloader",tags=["webloader"])


@webRouter.post("/url")
async def webloader(data:UrlSchema):
    response = await load_url(data.url)
    return {"status": "success Full Loaded"}