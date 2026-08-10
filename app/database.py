from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from fastapi import HTTPException

DATABASE_URL = ""

engine = create_engine(DATABASE_URL, echo = True)

SessionLocal = sessionmaker(bind = engine, autoflush = True)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal
    try:
        yield db
    except:
        raise HTTPException(
            status_code = 500, 
            detail = "Session not able to be created"
        )
    finally:
        db.close()

