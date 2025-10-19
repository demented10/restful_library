from pydantic import BaseModel, ConfigDict
from typing import Optional

class Book(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: Optional[int] = None
    cipher: str
    title: str
    first_author: str
    publication_year: int
    price: float
    copies_available: int
    publisher_id: int

class BookCreate(BaseModel):
    cipher: str
    title: str
    first_author: str
    publication_year: int
    price: float
    copies_available: int
    publisher_id: int

class BookUpdate(BaseModel):
    cipher: Optional[str] = None
    title: Optional[str] = None
    first_author: Optional[str] = None
    publication_year: Optional[int] = None
    price: Optional[float] = None
    copies_available: Optional[int] = None
    publisher_id: Optional[int] = None