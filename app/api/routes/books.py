from fastapi import APIRouter, Depends, HTTPException
from app.schemas.book import Book, BookCreate, BookUpdate
from app.services.book_service import BookService
from app.api.dependencies import get_book_service

router = APIRouter()

@router.get("/", response_model=list[Book])
def get_books(book_service: BookService = Depends(get_book_service)):
    return book_service.get_all_books()

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, book_service: BookService = Depends(get_book_service)):
    book = book_service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=Book)
def create_book(book_create: BookCreate, book_service: BookService = Depends(get_book_service)):
    try:
        return book_service.create_book(book_create)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate, book_service: BookService = Depends(get_book_service)):
    book = book_service.update_book(book_id, book_update)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, book_service: BookService = Depends(get_book_service)):
    if not book_service.delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

@router.get("/publisher/{publisher_id}", response_model=list[Book])
def get_books_by_publisher(publisher_id: int, book_service: BookService = Depends(get_book_service)):
    return book_service.get_books_by_publisher(publisher_id)