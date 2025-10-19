from pydantic import BaseModel, ConfigDict
from typing import Optional

class Reader(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: Optional[int] = None
    full_name: str
    address: str
    phone: str

class ReaderCreate(BaseModel):
    full_name: str
    address: str
    phone: str

class ReaderUpdate(BaseModel):
    full_name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None