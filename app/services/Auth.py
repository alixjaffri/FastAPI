from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserCreate
from app.repository.user import UserRepository
from fastapi import HTTPException
from app.security import hash_pwd, verify_pwd
from app.utils.auth import create_token

class AuthService:

    def __init__(self):
        self.repo = UserRepository

    def register(self, db: Session, data: UserCreate):
        if self.repo.get_by_email(db, data.email):
            return HTTPException(status= "400", detail = "User already exists")
        
        self.repo.create(db, UserCreate, hash_pwd(data.password))

    def login(self, db: Session, email: str, password: str):
        user = self.repo.get_by_email(db, email)

        if not user or not verify_pwd(password, user.hashed_password):
            return HTTPException(status = "401", detail = "Bad Credentials")
        
        return {"access token": create_token(user.id)}
