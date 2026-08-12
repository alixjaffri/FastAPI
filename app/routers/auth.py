from fastapi import APIRouter, HTTPException, Depends
from app.models.users import User
from app.schemas.users import UserCreate, UserRead
from app.database import get_db
from app.services.Auth import AuthService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix = "/auth", tags = ["auth"])

service = AuthService

@router.post("/register")
def register(data: UserCreate, db = Depends(get_db)):
    return service.register(db, data)

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):
    return service.login(db, form.username, form.password)




