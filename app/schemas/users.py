from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    email: str
    username: str
    password: str

class UserCreate(UserBase):
    pass

class UserRead(BaseModel):
    id: int
    email: str
    username: str
    password: str

    model_config = ConfigDict(
        from_attributes=True
    )

class TokenOut(BaseModel):
    access_token: str