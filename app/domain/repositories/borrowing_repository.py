from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.borrowing import Borrowing

class BorrowingRepository(ABC):
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Borrowing]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Borrowing]:
        pass
    
    @abstractmethod
    def create(self, borrowing: Borrowing) -> Borrowing:
        pass
    
    @abstractmethod
    def update(self, id: int, borrowing: Borrowing) -> Optional[Borrowing]:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def get_borrowings_by_reader(self, reader_id: int) -> List[Borrowing]:
        pass
    
    @abstractmethod
    def get_borrowings_by_book(self, book_id: int) -> List[Borrowing]:
        pass