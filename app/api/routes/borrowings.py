from fastapi import APIRouter, Depends, HTTPException
from app.schemas.borrowing import Borrowing, BorrowingCreate
from app.services.borrowing_service import BorrowingService
from app.api.dependencies import get_borrowing_service

router = APIRouter()

@router.get("/", response_model=list[Borrowing])
def get_borrowings(borrowing_service: BorrowingService = Depends(get_borrowing_service)):
    return borrowing_service.get_all_borrowings()

@router.get("/{borrowing_id}", response_model=Borrowing)
def get_borrowing(borrowing_id: int, borrowing_service: BorrowingService = Depends(get_borrowing_service)):
    borrowing = borrowing_service.get_borrowing(borrowing_id)
    if not borrowing:
        raise HTTPException(status_code=404, detail="Borrowing not found")
    return borrowing

@router.post("/", response_model=Borrowing)
def create_borrowing(borrowing_create: BorrowingCreate, borrowing_service: BorrowingService = Depends(get_borrowing_service)):
    try:
        return borrowing_service.borrow_book(borrowing_create)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{borrowing_id}")
def return_book(borrowing_id: int, borrowing_service: BorrowingService = Depends(get_borrowing_service)):
    if not borrowing_service.return_book(borrowing_id):
        raise HTTPException(status_code=404, detail="Borrowing not found")
    return {"message": "Book returned successfully"}

@router.get("/reader/{reader_id}", response_model=list[Borrowing])
def get_borrowings_by_reader(reader_id: int, borrowing_service: BorrowingService = Depends(get_borrowing_service)):
    return borrowing_service.get_borrowings_by_reader(reader_id)

@router.get("/book/{book_id}", response_model=list[Borrowing])
def get_borrowings_by_book(book_id: int, borrowing_service: BorrowingService = Depends(get_borrowing_service)):
    return borrowing_service.get_borrowings_by_book(book_id)

@router.get("/overdue/", response_model=list[Borrowing])
def get_overdue_borrowings(borrowing_service: BorrowingService = Depends(get_borrowing_service)):
    return borrowing_service.get_overdue_borrowings()