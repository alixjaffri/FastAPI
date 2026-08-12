from sqlalchemy import String, Text, Integer, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from datetime import datetime

class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    title: Mapped[str] = mapped_column(String(70), index = True)
    description: Mapped[str] = mapped_column(String(200), index = True)
    date_published: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        server_default = func.now(),
        index = True
    )