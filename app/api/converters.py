from app.schemas.book import BookCreate as SchemaBookCreate, BookUpdate as SchemaBookUpdate, Book as SchemaBook
from app.schemas.publisher import PublisherCreate as SchemaPublisherCreate, PublisherUpdate as SchemaPublisherUpdate, Publisher as SchemaPublisher
from app.schemas.reader import ReaderCreate as SchemaReaderCreate, ReaderUpdate as SchemaReaderUpdate, Reader as SchemaReader
from app.schemas.borrowing import BorrowingCreate as SchemaBorrowingCreate, Borrowing as SchemaBorrowing

from app.domain.models.book import BookCreate as DomainBookCreate, BookUpdate as DomainBookUpdate, Book as DomainBook
from app.domain.models.publisher import PublisherCreate as DomainPublisherCreate, PublisherUpdate as DomainPublisherUpdate, Publisher as DomainPublisher
from app.domain.models.reader import ReaderCreate as DomainReaderCreate, ReaderUpdate as DomainReaderUpdate, Reader as DomainReader
from app.domain.models.borrowing import BorrowingCreate as DomainBorrowingCreate, Borrowing as DomainBorrowing

# Book converters
def schema_book_create_to_domain(schema_book: SchemaBookCreate) -> DomainBookCreate:
    return DomainBookCreate(**schema_book.dict())

def schema_book_update_to_domain(schema_book: SchemaBookUpdate) -> DomainBookUpdate:
    return DomainBookUpdate(**schema_book.dict(exclude_unset=True))

def domain_book_to_schema(domain_book: DomainBook) -> SchemaBook:
    return SchemaBook(**domain_book.dict())

# Publisher converters
def schema_publisher_create_to_domain(schema_publisher: SchemaPublisherCreate) -> DomainPublisherCreate:
    return DomainPublisherCreate(**schema_publisher.dict())

def schema_publisher_update_to_domain(schema_publisher: SchemaPublisherUpdate) -> DomainPublisherUpdate:
    return DomainPublisherUpdate(**schema_publisher.dict(exclude_unset=True))

def domain_publisher_to_schema(domain_publisher: DomainPublisher) -> SchemaPublisher:
    return SchemaPublisher(**domain_publisher.dict())

# Reader converters
def schema_reader_create_to_domain(schema_reader: SchemaReaderCreate) -> DomainReaderCreate:
    return DomainReaderCreate(**schema_reader.dict())

def schema_reader_update_to_domain(schema_reader: SchemaReaderUpdate) -> DomainReaderUpdate:
    return DomainReaderUpdate(**schema_reader.dict(exclude_unset=True))

def domain_reader_to_schema(domain_reader: DomainReader) -> SchemaReader:
    return SchemaReader(**domain_reader.dict())

# Borrowing converters
def schema_borrowing_create_to_domain(schema_borrowing: SchemaBorrowingCreate) -> DomainBorrowingCreate:
    return DomainBorrowingCreate(**schema_borrowing.dict())

def domain_borrowing_to_schema(domain_borrowing: DomainBorrowing) -> SchemaBorrowing:
    return SchemaBorrowing(**domain_borrowing.dict())