from sqlalchemy.orm import Session
from models.users import User
from schemas.users import UserCreate
from typing import Optional

class UserRepository:

    def __init__(self, db:Session):
        self.db = db
            
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def create(self, db: Session, data: UserCreate, hashed_pwd) -> Optional[User]:
        user = User(
            email = data.email,
            username = data.username,
            hashed_password = hashed_pwd
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user