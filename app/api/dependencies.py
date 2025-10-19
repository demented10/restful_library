from app.infrastructure.database import get_db
from app.infrastructure.database.repositories.sqlalchemy import (
    SQLAlchemyBookRepository,
    SQLAlchemyPublisherRepository,
    SQLAlchemyReaderRepository,
    SQLAlchemyBorrowingRepository
)
from app.services import (
    BookService,
    PublisherService,
    ReaderService,
    BorrowingService,
    ReportService
)

def get_book_service():
    db = next(get_db())
    book_repository = SQLAlchemyBookRepository(db)
    return BookService(book_repository)

def get_publisher_service():
    db = next(get_db())
    publisher_repository = SQLAlchemyPublisherRepository(db)
    return PublisherService(publisher_repository)

def get_reader_service():
    db = next(get_db())
    reader_repository = SQLAlchemyReaderRepository(db)
    return ReaderService(reader_repository)

def get_borrowing_service():
    db = next(get_db())
    borrowing_repository = SQLAlchemyBorrowingRepository(db)
    book_repository = SQLAlchemyBookRepository(db)
    reader_repository = SQLAlchemyReaderRepository(db)
    return BorrowingService(borrowing_repository, book_repository, reader_repository)

def get_report_service():
    db = next(get_db())
    borrowing_repository = SQLAlchemyBorrowingRepository(db)
    book_repository = SQLAlchemyBookRepository(db)
    reader_repository = SQLAlchemyReaderRepository(db)
    return ReportService(borrowing_repository, book_repository, reader_repository)