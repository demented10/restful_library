from pydantic import BaseModel, ConfigDict
from typing import Optional

class ReaderBase(BaseModel):
    full_name: str
    address: str
    phone: str

class ReaderCreate(ReaderBase):
    pass

class ReaderUpdate(BaseModel):
    full_name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None

class Reader(ReaderBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int