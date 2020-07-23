from fastapi import FastAPI, Request, Response
from api.api_v1.api import api_router
import uvicorn
from core.config import settings
from database import Base, engine, SessionLocal
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

Base.metadata.create_all(bind=engine)

app = FastAPI(title="myapp")

app.mount("/static", StaticFiles(directory="static"), name="static")
# 载入模板 模板中存放html，静态文件中存放css和js
templates = Jinja2Templates(directory="templates")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/items/{id}")
async def read_item(request: Request, id: str):
    # 模板渲染返回的数据
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
