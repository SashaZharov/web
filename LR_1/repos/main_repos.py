from fastapi import HTTPException

from db.db import session
from models.main_models import *


class LibraryRepository:
    def get_library(self, library_id: int):
        library = session.get(Library, library_id)
        if not library:
            raise HTTPException(status_code=404, detail="Balance not found")
        return library


class AuthorRepository:
    def create_author(self, author: AuthorCreate):
        db_author = Author(**author.dict())
        session.add(db_author)
        session.commit()
        session.refresh(db_author)
        return db_author

    def get_all_authors(self):
        return session.query(Author).all()

    def update_author(self, author_id: int, author: AuthorUpdate):
        db_author = session.get(Author, author_id)
        if db_author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        for key, value in author.dict(exclude_unset=True).items():
            setattr(db_author, key, value)
        session.add(db_author)
        session.commit()
        session.refresh(db_author)
        return db_author


class BookRepository:
    def create_book(self, book: BookCreate):
        db_book = Book(**book.dict())
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
        return db_book

    def get_all_books(self):
        return session.query(Book).all()

    def update_book(self, book_id: int, book: BookUpdate):
        db_book = session.get(Book, book_id)
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        for key, value in book.dict(exclude_unset=True).items():
            setattr(db_book, key, value)
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
        return db_book


class ExchangeRequestRepository:
    def get_all_exchange_requests(self):
        return session.query(ExchangeRequest).all()

    def create_exchange_request(self, exchange_request: ExchangeRequestCreate):
        db_exchange_request = ExchangeRequest(**exchange_request.dict())
        session.add(db_exchange_request)
        session.commit()
        session.refresh(db_exchange_request)
        return db_exchange_request

    def update_exchange_request(self, exchange_request_id: int, exchange_request: ExchangeRequestUpdate):
        db_exchange_request = session.get(ExchangeRequest, exchange_request_id)
        if db_exchange_request is None:
            raise HTTPException(status_code=404, detail="Exchange request not found")
        for key, value in exchange_request.dict(exclude_unset=True).items():
            setattr(db_exchange_request, key, value)
        session.add(db_exchange_request)
        session.commit()
        session.refresh(db_exchange_request)
        return db_exchange_request
