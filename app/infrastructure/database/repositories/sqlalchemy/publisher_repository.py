from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.models.publisher import Publisher
from app.domain.repositories.publisher_repository import PublisherRepository
from app.infrastructure.database.models.publisher import PublisherModel

class SQLAlchemyPublisherRepository(PublisherRepository):
    def __init__(self, session: Session):
        self.session = session
        self.model = PublisherModel

    def _to_domain(self, db_model: PublisherModel) -> Optional[Publisher]:
        if db_model is None:
            return None
        return Publisher(
            id=db_model.id,
            name=db_model.name,
            city=db_model.city
        )

    def get_by_id(self, id: int) -> Optional[Publisher]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        return self._to_domain(db_model)

    def get_all(self) -> List[Publisher]:
        db_models = self.session.query(self.model).all()
        return [self._to_domain(model) for model in db_models if model is not None]

    def create(self, publisher: Publisher) -> Publisher:
        db_model = self.model(
            name=publisher.name,
            city=publisher.city
        )
        self.session.add(db_model)
        self.session.commit()
        self.session.refresh(db_model)
        return self._to_domain(db_model)

    def update(self, id: int, publisher: Publisher) -> Optional[Publisher]:
        db_model = self.session.query(self.model).filter(self.model.id == id).first()
        if db_model:
            db_model.name = publisher.name
            db_model.city = publisher.city
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