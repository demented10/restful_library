from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    cipher = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    first_author = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    copies_available = Column(Integer, nullable=False, default=0)
    publisher_id = Column(Integer, ForeignKey("publishers.id"), nullable=False)
    
    # Связи
    publisher = relationship("PublisherModel", back_populates="books")
    borrowings = relationship("BorrowingModel", back_populates="book")