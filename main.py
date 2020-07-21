from fastapi import FastAPI
from api.api_v1.api import api_router
import uvicorn
from core.config import settings


app = FastAPI(title="myapp")

app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
