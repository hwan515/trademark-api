from fastapi import FastAPI
from app.routes import trademark

app = FastAPI(title="상표 검색 API")
app.include_router(trademark.router, prefix="/api")
