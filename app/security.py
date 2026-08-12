from passlib.context import CryptContext

pwd = CryptContext(schemes = "bcrypt", deprecated = "auto")

def hash_pwd(p: str):
    return pwd.hash(p)

def verify_pwd(p: str, h: str):
    return pwd.verify(p, h) # verify password with the stored hash of the password