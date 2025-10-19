from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.models.borrowing import Borrowing
from app.domain.repositories.borrowing_repository import BorrowingRepository
from app.infrastructure.database.models.borrowing import BorrowingModel

class SQLAlchemyBorrowingRepository(BorrowingRepository):
    def __init__(self, session: Session):
        self.session = session
        self.model = BorrowingModel

    def _to_domain(self, db_model: BorrowingModel) -> Optional[Borrowing]:
        if db_model is None:
            return None
        return Borrowing(
            id=db_model.id,
            reader_id=db_model.reader_id,
            book_id=db_model.book_id,
            borrow_date=db_model.borrow_date
        )

    def get_by_id(self, id: int) -> Optional[Borrowing]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        return self._to_domain(db_model)

    def get_all(self) -> List[Borrowing]:
        db_models = self.session.query(self.model).all()
        return [self._to_domain(model) for model in db_models if model is not None]

    def create(self, borrowing: Borrowing) -> Borrowing:
        db_model = self.model(
            reader_id=borrowing.reader_id,
            book_id=borrowing.book_id,
            borrow_date=borrowing.borrow_date
        )
        self.session.add(db_model)
        self.session.commit()
        self.session.refresh(db_model)
        return self._to_domain(db_model)

    def update(self, id: int, borrowing: Borrowing) -> Optional[Borrowing]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        if db_model:
            db_model.reader_id = borrowing.reader_id
            db_model.book_id = borrowing.book_id
            db_model.borrow_date = borrowing.borrow_date
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

    def get_borrowings_by_reader(self, reader_id: int) -> List[Borrowing]:
        db_models = self.session.query(self.model).filter(self.model.reader_id == reader_id).all()
        return [self._to_domain(model) for model in db_models if model is not None]

    def get_borrowings_by_book(self, book_id: int) -> List[Borrowing]:
        db_models = self.session.query(self.model).filter(self.model.book_id == book_id).all()
        return [self._to_domain(model) for model in db_models if model is not None]