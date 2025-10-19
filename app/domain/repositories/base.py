from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar("T")
K = TypeVar("K")


class BaseRepository(Generic[T, K], ABC):
    @abstractmethod
    def get_by_id(self, id: K) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def update(self, id: K, entity: T) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, id: K) -> bool:
        pass
