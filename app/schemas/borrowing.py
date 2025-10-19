from pydantic import BaseModel, ConfigDict
from datetime import date

class BorrowingBase(BaseModel):
    reader_id: int
    book_id: int
    borrow_date: date

class BorrowingCreate(BorrowingBase):
    pass

class Borrowing(BorrowingBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int