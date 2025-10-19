from pydantic import BaseModel, ConfigDict
from typing import Optional

class Publisher(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: Optional[int] = None
    name: str
    city: str

class PublisherCreate(BaseModel):
    name: str
    city: str

class PublisherUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None