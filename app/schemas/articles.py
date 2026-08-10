from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ArticleBase(BaseModel):
    title: str
    description: str

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

class ArticleRead(BaseModel):
    id: int
    title: str
    description: str
    date_published: datetime

    model_config = ConfigDict(from_attributes = True)