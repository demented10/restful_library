from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class PublisherModel(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    city = Column(String, nullable=False)
    
    # Связь с книгами
    books = relationship("BookModel", back_populates="publisher")