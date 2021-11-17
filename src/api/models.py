import datetime
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field()
    email: str = Field()
    password: str = Field()


class UpdateUserPass(BaseModel):
    id: int
    password: str


class SearchUser(BaseModel):
    id: Optional[int]
    username: Optional[str]
    email: Optional[str]


class UserDB(User):
    id: int
