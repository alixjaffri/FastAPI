from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.article import Article
from app.schemas.articles import ArticleCreate, ArticleUpdate
from app.repository.articles import ArticleRepository

class ArticleService:

    def __init__(self):
        self.repo = ArticleRepository

    def create_article(self, db: Session, data: ArticleCreate):
        return self.repo.create(db, data)
    
    def get_article(self, db: Session, article_id: int):
        article = self.repo.get_by_id(db, article_id)
        if not article:
            raise HTTPException(status_code = 404, detail = "Article not found")
        else:
            return article
        
    def get_all_articles(self, db: Session):
        return self.repo.get_all(db)
    
    def update_article(self, db: Session, article_id: int, data: ArticleUpdate):
        article = self.get_article(db, article_id)
        return self.repo.update(db, article, data)
    
    def delete_article(self, db: Session, article_id: int):
        article = self.get_article(db, article_id)
        return self.repo.delete(db, article)
    
    
