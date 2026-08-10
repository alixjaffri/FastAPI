from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index = True)
    email: Mapped[str] = mapped_column(String(200), unique=True, index = True)
    username: Mapped[str] = mapped_column(String(100), index = True)
    hashed_password: Mapped[str] = mapped_column(String(255), index = True)
