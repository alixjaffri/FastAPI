from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from app.models.users import User
from app.utils.auth import decode_token
from app.database import get_db

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2), db = Depends(get_db)):
    try:
        data=decode_token(token)
        user_id = int(data["sub"])
    except:
        raise HTTPException(status = "401", detail = "Invalid Token")
    
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(401, "User not found")
    
    return user
