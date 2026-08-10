from passlib import CryptContext

pwd = CryptContext(schemas = "bcrypt", deprecated = "auto")

def hash_pwd(p: str):
    return pwd.hash(p)

def verify_pwd(p: str, h: str):
    return pwd.verify(p, h) # verify password with the stored hash of the password