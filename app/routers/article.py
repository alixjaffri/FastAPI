from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.article import ArticleService
from app.schemas.articles import ArticleCreate, ArticleUpdate, ArticleRead
from app.database import get_db
from app.deps import get_current_user

router = APIRouter(prefix = "/articles", tags = ["articles"])
service = ArticleService

@router.post("/", response_model = ArticleRead)
def create_article(data: ArticleCreate, user = Depends(get_current_user), db: Session = Depends(get_db)):
    return service.create_article(db, data)


@router.get("/{article_id}", response_model = ArticleRead)
def get_article(article_id: int, db: Session = Depends(get_db)):
    return service.get_article(article_id, db)


@router.get("/", response_model = list[ArticleRead])
def get_all_article(db: Session = Depends(get_db)):
    return service.get_all_articles(db)


@router.put("/{article_id}", response_model = ArticleRead)
def update_article(article_id: int, data: ArticleUpdate, db: Session = Depends(get_db)):
    return service.update_article(db, article_id, data)


@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    return service.delete_article(db, article_id)


