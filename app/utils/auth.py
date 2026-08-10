from jose import jwt
from datetime import datetime, timedelta

SECRET = "my_secret"
ALG = "HS256"

def create_token(user_id: int):
    payload = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(minutes = 60)
    }
    return jwt.encode(payload, SECRET, ALG)

def decode_token(token: str):
    return jwt.decode(token, SECRET, algorithms = [ALG])

