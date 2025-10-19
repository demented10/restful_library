from typing import List, Optional
from datetime import date, timedelta
from app.domain.models.borrowing import Borrowing, BorrowingCreate
from app.domain.repositories.borrowing_repository import BorrowingRepository
from app.domain.repositories.book_repository import BookRepository
from app.domain.repositories.reader_repository import ReaderRepository

class BorrowingService:
    def __init__(
        self, 
        borrowing_repository: BorrowingRepository,
        book_repository: BookRepository,
        reader_repository: ReaderRepository
    ):
        self.borrowing_repository = borrowing_repository
        self.book_repository = book_repository
        self.reader_repository = reader_repository

    def get_borrowing(self, borrowing_id: int) -> Optional[Borrowing]:
        return self.borrowing_repository.get_by_id(borrowing_id)

    def get_all_borrowings(self) -> List[Borrowing]:
        return self.borrowing_repository.get_all()

    def borrow_book(self, borrowing_create: BorrowingCreate) -> Borrowing:
        # Проверка существования книги
        book = self.book_repository.get_by_id(borrowing_create.book_id)
        if not book:
            raise ValueError("Book not found")
        
        # Проверка существования читателя
        reader = self.reader_repository.get_by_id(borrowing_create.reader_id)
        if not reader:
            raise ValueError("Reader not found")
        
        # Проверка доступности книги
        if book.copies_available <= 0:
            raise ValueError("No copies available")
        
        # Проверка лимита книг у читателя (максимум 5)
        reader_borrowings = self.borrowing_repository.get_borrowings_by_reader(borrowing_create.reader_id)
        if len(reader_borrowings) >= 5:
            raise ValueError("Reader has reached the borrowing limit (5 books)")
        
        # Создание записи о выдаче
        borrowing_data = borrowing_create.model_dump()
        borrowing = Borrowing(**borrowing_data)
        created_borrowing = self.borrowing_repository.create(borrowing)
        
        # Уменьшение количества доступных экземпляров
        book.copies_available -= 1
        self.book_repository.update(book.id, book)
        
        return created_borrowing

    def return_book(self, borrowing_id: int) -> bool:
        borrowing = self.borrowing_repository.get_by_id(borrowing_id)
        if not borrowing:
            return False
        
        # Увеличение количества доступных экземпляров
        book = self.book_repository.get_by_id(borrowing.book_id)
        if book:
            book.copies_available += 1
            self.book_repository.update(book.id, book)
        
        # Удаление записи о выдаче
        return self.borrowing_repository.delete(borrowing_id)

    def get_overdue_borrowings(self) -> List[Borrowing]:
        all_borrowings = self.borrowing_repository.get_all()
        overdue_borrowings = []
        
        for borrowing in all_borrowings:
            due_date = borrowing.borrow_date + timedelta(days=20)
            if date.today() > due_date:
                overdue_borrowings.append(borrowing)
        
        return overdue_borrowings

    def get_borrowings_by_reader(self, reader_id: int) -> List[Borrowing]:
        return self.borrowing_repository.get_borrowings_by_reader(reader_id)

    def get_borrowings_by_book(self, book_id: int) -> List[Borrowing]:
        return self.borrowing_repository.get_borrowings_by_book(book_id)