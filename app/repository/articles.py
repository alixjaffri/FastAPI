from sqlalchemy.orm import Session
from app.models.article import Article
from app.schemas.articles import ArticleCreate, ArticleUpdate
from typing import Optional

class ArticleRepository:

    def __init__(self, db: Session):
        self.db = db

    # Create (POST)
    def create(self, db: Session, data: ArticleCreate) -> Optional[Article]:
        article = Article(
            title = data.title,
            description = data.description
        )

        db.add(article)
        db.commit()
        db.refresh(article)
        return article
    
    # GET
    def get_by_id(self, db: Session, article_id: int) -> Optional[Article]:
        return db.query(Article).filter(Article.id == article_id).first()
    
    # GET ALL
    def get_all(self, db: Session) -> list[Article]:
        return db.query(Article).all()
    
    # Update (PUT)
    def update(self, db: Session, article: Article, data: ArticleUpdate) -> Optional[Article]:
        
        update_article = data.model_dump(exclude_unset = True) # exclude_unset = True says to not put the fields not given by user = None
        for field, value in update_article.items():
            setattr(article, field, value)

        db.commit()
        db.refresh(article)
        return article
    
    # DELETE
    def delete(self, db: Session, article: Article) -> bool:
        
        db.delete(article)
        db.commit()
        return True