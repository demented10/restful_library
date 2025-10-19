from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.publisher import Publisher

class PublisherRepository(ABC):
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Publisher]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Publisher]:
        pass
    
    @abstractmethod
    def create(self, publisher: Publisher) -> Publisher:
        pass
    
    @abstractmethod
    def update(self, id: int, publisher: Publisher) -> Optional[Publisher]:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass