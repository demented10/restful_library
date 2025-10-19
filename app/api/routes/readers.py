from fastapi import APIRouter, Depends, HTTPException
from app.schemas.reader import Reader, ReaderCreate, ReaderUpdate
from app.services.reader_service import ReaderService
from app.api.dependencies import get_reader_service

router = APIRouter()

@router.get("/", response_model=list[Reader])
def get_readers(reader_service: ReaderService = Depends(get_reader_service)):
    return reader_service.get_all_readers()

@router.get("/{reader_id}", response_model=Reader)
def get_reader(reader_id: int, reader_service: ReaderService = Depends(get_reader_service)):
    reader = reader_service.get_reader(reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return reader

@router.post("/", response_model=Reader)
def create_reader(reader_create: ReaderCreate, reader_service: ReaderService = Depends(get_reader_service)):
    return reader_service.create_reader(reader_create)

@router.put("/{reader_id}", response_model=Reader)
def update_reader(reader_id: int, reader_update: ReaderUpdate, reader_service: ReaderService = Depends(get_reader_service)):
    reader = reader_service.update_reader(reader_id, reader_update)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return reader

@router.delete("/{reader_id}")
def delete_reader(reader_id: int, reader_service: ReaderService = Depends(get_reader_service)):
    if not reader_service.delete_reader(reader_id):
        raise HTTPException(status_code=404, detail="Reader not found")
    return {"message": "Reader deleted successfully"}