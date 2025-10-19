from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class Borrowing(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: Optional[int] = None
    reader_id: int
    book_id: int
    borrow_date: date

class BorrowingCreate(BaseModel):
    reader_id: int
    book_id: int
    borrow_date: date