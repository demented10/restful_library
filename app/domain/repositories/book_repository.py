from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.book import Book

class BookRepository(ABC):
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Book]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Book]:
        pass
    
    @abstractmethod
    def create(self, book: Book) -> Book:
        pass
    
    @abstractmethod
    def update(self, id: int, book: Book) -> Optional[Book]:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def get_by_cipher(self, cipher: str) -> Optional[Book]:
        pass
    
    @abstractmethod
    def get_books_by_publisher(self, publisher_id: int) -> List[Book]:
        pass