from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.reader import Reader

class ReaderRepository(ABC):
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Reader]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Reader]:
        pass
    
    @abstractmethod
    def create(self, reader: Reader) -> Reader:
        pass
    
    @abstractmethod
    def update(self, id: int, reader: Reader) -> Optional[Reader]:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass