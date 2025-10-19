from typing import List, Optional
from app.domain.models.publisher import Publisher, PublisherCreate, PublisherUpdate
from app.domain.repositories.publisher_repository import PublisherRepository

class PublisherService:
    def __init__(self, publisher_repository: PublisherRepository):
        self.publisher_repository = publisher_repository

    def get_publisher(self, publisher_id: int) -> Optional[Publisher]:
        return self.publisher_repository.get_by_id(publisher_id)

    def get_all_publishers(self) -> List[Publisher]:
        return self.publisher_repository.get_all()

    def create_publisher(self, publisher_create: PublisherCreate) -> Publisher:
        publisher_data = publisher_create.model_dump()
        publisher = Publisher(**publisher_data)
        return self.publisher_repository.create(publisher)

    def update_publisher(self, publisher_id: int, publisher_update: PublisherUpdate) -> Optional[Publisher]:
        existing_publisher = self.publisher_repository.get_by_id(publisher_id)
        if not existing_publisher:
            return None
        
        update_data = publisher_update.model_dump(exclude_unset=True)
        updated_publisher_data = {**existing_publisher.model_dump(), **update_data}
        updated_publisher = Publisher(**updated_publisher_data)
        return self.publisher_repository.update(publisher_id, updated_publisher)

    def delete_publisher(self, publisher_id: int) -> bool:
        return self.publisher_repository.delete(publisher_id)