from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.models.book import Book
from app.domain.repositories.book_repository import BookRepository
from app.infrastructure.database.models.book import BookModel

class SQLAlchemyBookRepository(BookRepository):
    def __init__(self, session: Session):
        self.session = session
        self.model = BookModel

    def _to_domain(self, db_model: BookModel) -> Optional[Book]:
        if db_model is None:
            return None
        return Book.model_validate({
            "id": db_model.id,
            "cipher": db_model.cipher,
            "title": db_model.title,
            "first_author": db_model.first_author,
            "publication_year": db_model.publication_year,
            "price": db_model.price,
            "copies_available": db_model.copies_available,
            "publisher_id": db_model.publisher_id
        })

    def get_by_id(self, id: int) -> Optional[Book]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        return self._to_domain(db_model)

    def get_all(self) -> List[Book]:
        db_models = self.session.query(self.model).all()
        return [self._to_domain(model) for model in db_models if model is not None]

    def create(self, book: Book) -> Book:
        db_model = self.model(
            cipher=book.cipher,
            title=book.title,
            first_author=book.first_author,
            publication_year=book.publication_year,
            price=book.price,
            copies_available=book.copies_available,
            publisher_id=book.publisher_id
        )
        self.session.add(db_model)
        self.session.commit()
        self.session.refresh(db_model)
        return self._to_domain(db_model)

    def update(self, id: int, book: Book) -> Optional[Book]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        if db_model:
            db_model.cipher = book.cipher
            db_model.title = book.title
            db_model.first_author = book.first_author
            db_model.publication_year = book.publication_year
            db_model.price = book.price
            db_model.copies_available = book.copies_available
            db_model.publisher_id = book.publisher_id
            self.session.commit()
            self.session.refresh(db_model)
            return self._to_domain(db_model)
        return None

    def delete(self, id: int) -> bool:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        if db_model:
            self.session.delete(db_model)
            self.session.commit()
            return True
        return False

    def get_by_cipher(self, cipher: str) -> Optional[Book]:
        db_model = self.session.query(self.model).filter(self.model.cipher == cipher).first()
        return self._to_domain(db_model)

    def get_books_by_publisher(self, publisher_id: int) -> List[Book]:
        db_models = self.session.query(self.model).filter(self.model.publisher_id == publisher_id).all()
        return [self._to_domain(model) for model in db_models if model is not None]