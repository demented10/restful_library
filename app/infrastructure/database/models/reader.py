from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class ReaderModel(Base):
    __tablename__ = "readers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    
    # Связь с выдачами
    borrowings = relationship("BorrowingModel", back_populates="reader")