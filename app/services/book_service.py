from typing import List, Optional
from app.domain.models.book import Book, BookCreate, BookUpdate
from app.domain.repositories.book_repository import BookRepository

class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def get_book(self, book_id: int) -> Optional[Book]:
        return self.book_repository.get_by_id(book_id)

    def get_all_books(self) -> List[Book]:
        return self.book_repository.get_all()

    def create_book(self, book_create: BookCreate) -> Book:
        # Проверка на уникальность шифра
        existing_book = self.book_repository.get_by_cipher(book_create.cipher)
        if existing_book:
            raise ValueError(f"Book with cipher '{book_create.cipher}' already exists")
        
        # Создаем книгу без id
        book_data = book_create.model_dump()
        book = Book(**book_data)
        return self.book_repository.create(book)

    def update_book(self, book_id: int, book_update: BookUpdate) -> Optional[Book]:
        existing_book = self.book_repository.get_by_id(book_id)
        if not existing_book:
            return None
        
        update_data = book_update.model_dump(exclude_unset=True)
        # Создаем обновленную книгу с сохранением id
        updated_book_data = {**existing_book.model_dump(), **update_data}
        updated_book = Book(**updated_book_data)
        return self.book_repository.update(book_id, updated_book)

    def delete_book(self, book_id: int) -> bool:
        return self.book_repository.delete(book_id)

    def get_books_by_publisher(self, publisher_id: int) -> List[Book]:
        return self.book_repository.get_books_by_publisher(publisher_id)