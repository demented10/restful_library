from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.models.reader import Reader
from app.domain.repositories.reader_repository import ReaderRepository
from app.infrastructure.database.models.reader import ReaderModel

class SQLAlchemyReaderRepository(ReaderRepository):
    def __init__(self, session: Session):
        self.session = session
        self.model = ReaderModel

    def _to_domain(self, db_model: ReaderModel) -> Optional[Reader]:
        if db_model is None:
            return None
        return Reader(
            id=db_model.id,
            full_name=db_model.full_name,
            address=db_model.address,
            phone=db_model.phone
        )

    def get_by_id(self, id: int) -> Optional[Reader]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        return self._to_domain(db_model)

    def get_all(self) -> List[Reader]:
        db_models = self.session.query(self.model).all()
        return [self._to_domain(model) for model in db_models if model is not None]

    def create(self, reader: Reader) -> Reader:
        db_model = self.model(
            full_name=reader.full_name,
            address=reader.address,
            phone=reader.phone
        )
        self.session.add(db_model)
        self.session.commit()
        self.session.refresh(db_model)
        return self._to_domain(db_model)

    def update(self, id: int, reader: Reader) -> Optional[Reader]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        if db_model:
            db_model.full_name = reader.full_name
            db_model.address = reader.address
            db_model.phone = reader.phone
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