from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.core.database import Base

class BorrowingModel(Base):
    __tablename__ = "borrowings"

    id = Column(Integer, primary_key=True, index=True)
    reader_id = Column(Integer, ForeignKey("readers.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    borrow_date = Column(Date, nullable=False)
    
    # Связи
    reader = relationship("ReaderModel", back_populates="borrowings")
    book = relationship("BookModel", back_populates="borrowings")