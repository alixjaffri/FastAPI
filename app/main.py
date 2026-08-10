from fastapi import FastAPI
from app.database import Base, engine
from app.routers.article import router as article_router
from app.routers.auth import router as auth_router

app = FastAPI(
    title = "Articles CRUD aaplication",
    description = "Articles CRUD based in FastAPI"
)

Base.metadata.create_all(bind = engine)

app.include_router(
    article_router
)

app.include_router(
    auth_router
)

