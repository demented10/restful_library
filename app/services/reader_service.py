from typing import List, Optional
from app.domain.models.reader import Reader, ReaderCreate, ReaderUpdate
from app.domain.repositories.reader_repository import ReaderRepository

class ReaderService:
    def __init__(self, reader_repository: ReaderRepository):
        self.reader_repository = reader_repository

    def get_reader(self, reader_id: int) -> Optional[Reader]:
        return self.reader_repository.get_by_id(reader_id)

    def get_all_readers(self) -> List[Reader]:
        return self.reader_repository.get_all()

    def create_reader(self, reader_create: ReaderCreate) -> Reader:
        reader_data = reader_create.model_dump()
        reader = Reader(**reader_data)
        return self.reader_repository.create(reader)

    def update_reader(self, reader_id: int, reader_update: ReaderUpdate) -> Optional[Reader]:
        existing_reader = self.reader_repository.get_by_id(reader_id)
        if not existing_reader:
            return None
        
        update_data = reader_update.model_dump(exclude_unset=True)
        updated_reader_data = {**existing_reader.model_dump(), **update_data}
        updated_reader = Reader(**updated_reader_data)
        return self.reader_repository.update(reader_id, updated_reader)

    def delete_reader(self, reader_id: int) -> bool:
        return self.reader_repository.delete(reader_id)