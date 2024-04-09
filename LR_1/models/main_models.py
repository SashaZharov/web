from enum import Enum
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from models.user_models import User


class AuthorDefault(SQLModel):
    name: str
    birth_year: int


class Author(AuthorDefault, table=True):
    id: int = Field(primary_key=True)
    books: List['Book'] = Relationship(back_populates="author")


class AuthorCreate(AuthorDefault):
    pass


class AuthorUpdate(AuthorDefault):
    pass


class LibraryDefault(SQLModel):
    user_id: Optional[int] = Field(foreign_key="user.id")


class Library(LibraryDefault, table=True):
    id: int = Field(primary_key=True)
    user: Optional[User] = Relationship(back_populates="library")
    books: List['Book'] = Relationship(back_populates="library")


class UserLibrary(LibraryDefault):
    books: List['Book'] = None


class BookDefault(SQLModel):
    title: str
    published_year: int


class Book(BookDefault, table=True):
    id: int = Field(primary_key=True)
    author_id: int = Field(foreign_key="author.id")
    library_id: int = Field(foreign_key="library.id")
    author: Optional[Author] = Relationship(back_populates="books")
    library: Optional[Library] = Relationship(back_populates="books")


class UserBook(BookDefault):
    author: Optional[Author] = None


class BookCreate(BookDefault):
    author_id: int
    library_id: int


class BookUpdate(BookDefault):
    pass


class ExchangeRequest(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="exchangerequest")
    book_title: str


class ExchangeRequestCreate(SQLModel):
    user_id: int
    book_title: str


class ExchangeRequestUpdate(SQLModel):
    user_id: int
    book_title: str
