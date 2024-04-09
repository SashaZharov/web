from fastapi import APIRouter, HTTPException
from typing import List
from repos.main_repos import AuthorRepository, BookRepository, ExchangeRequestRepository, LibraryRepository
from models.main_models import *

main_router = APIRouter()
library_repository = LibraryRepository()
author_repository = AuthorRepository()
book_repository = BookRepository()
exchange_request_repository = ExchangeRequestRepository()


@main_router.get("/library/{library_id}", response_model=UserLibrary)
def get_library(library_id: int):
    return library_repository.get_library(library_id)


@main_router.post("/authors/", response_model=Author)
def create_author(author: AuthorCreate):
    return author_repository.create_author(author)


@main_router.get("/authors/", response_model=List[Author])
def get_all_authors():
    return author_repository.get_all_authors()


@main_router.put("/authors/{author_id}", response_model=Author)
def update_author(author_id: int, author: AuthorUpdate):
    return author_repository.update_author(author_id, author)


@main_router.post("/books/", response_model=Book)
def create_books(book: BookCreate):
    return book_repository.create_book(book)


@main_router.get("/books/", response_model=List[UserBook])
def get_all__book():
    return book_repository.get_all_books()


@main_router.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate):
    return book_repository.update_book(book_id, book)


@main_router.get("/exchange_requests/", response_model=List[ExchangeRequest])
def get_all_exchange_requests():
    return exchange_request_repository.get_all_exchange_requests()


@main_router.post("/exchange_requests/", response_model=ExchangeRequest)
def create_exchange_request(exchange_request: ExchangeRequestCreate):
    return exchange_request_repository.create_exchange_request(exchange_request)


@main_router.put("/exchange_requests/{exchange_request_id}", response_model=ExchangeRequest)
def update_exchange_request(exchange_request_id: int, exchange_request: ExchangeRequestUpdate):
    return exchange_request_repository.update_exchange_request(exchange_request_id, exchange_request)
