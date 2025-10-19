from typing import List, Optional, Generic, TypeVar
from sqlalchemy.orm import Session
from app.domain.repositories.base import BaseRepository

ModelType = TypeVar('ModelType')
DomainType = TypeVar('DomainType')

class SQLAlchemyRepository(BaseRepository[DomainType, int], Generic[ModelType, DomainType]):
    def __init__(self, session: Session, model: type[ModelType]):
        self.session = session
        self.model = model

    def _to_domain(self, db_model: ModelType) -> Optional[DomainType]:
        if db_model is None:
            return None
        return DomainType.from_orm(db_model)

    def get_by_id(self, id: int) -> Optional[DomainType]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        return self._to_domain(db_model)

    def get_all(self) -> List[DomainType]:
        db_models = self.session.query(self.model).all()
        return [self._to_domain(model) for model in db_models]

    def create(self, entity: DomainType) -> DomainType:
        db_model = self.model(**entity.dict())
        self.session.add(db_model)
        self.session.commit()
        self.session.refresh(db_model)
        return self._to_domain(db_model)

    def update(self, id: int, entity: DomainType) -> Optional[DomainType]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        if db_model:
            for key, value in entity.dict(exclude_unset=True).items():
                setattr(db_model, key, value)
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