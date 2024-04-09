import datetime
from typing import Optional
from pydantic import validator
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(index=True)
    password: str
    library: Optional["Library"] = Relationship(back_populates="user")
    exchangerequest: list["ExchangeRequest"] = Relationship(back_populates="user")
    created_at: datetime.datetime = Field(default=datetime.datetime.now())


class UserInput(SQLModel):
    username: str
    password: str
    password2: str

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords don\'t match')
        return v


class UserLogin(SQLModel):
    username: str
    password: str

