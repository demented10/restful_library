from fastapi import APIRouter, Depends, HTTPException
from app.schemas.publisher import Publisher, PublisherCreate, PublisherUpdate
from app.services.publisher_service import PublisherService
from app.api.dependencies import get_publisher_service

router = APIRouter()

@router.get("/", response_model=list[Publisher])
def get_publishers(publisher_service: PublisherService = Depends(get_publisher_service)):
    return publisher_service.get_all_publishers()

@router.get("/{publisher_id}", response_model=Publisher)
def get_publisher(publisher_id: int, publisher_service: PublisherService = Depends(get_publisher_service)):
    publisher = publisher_service.get_publisher(publisher_id)
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher

@router.post("/", response_model=Publisher)
def create_publisher(publisher_create: PublisherCreate, publisher_service: PublisherService = Depends(get_publisher_service)):
    return publisher_service.create_publisher(publisher_create)

@router.put("/{publisher_id}", response_model=Publisher)
def update_publisher(publisher_id: int, publisher_update: PublisherUpdate, publisher_service: PublisherService = Depends(get_publisher_service)):
    publisher = publisher_service.update_publisher(publisher_id, publisher_update)
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher

@router.delete("/{publisher_id}")
def delete_publisher(publisher_id: int, publisher_service: PublisherService = Depends(get_publisher_service)):
    if not publisher_service.delete_publisher(publisher_id):
        raise HTTPException(status_code=404, detail="Publisher not found")
    return {"message": "Publisher deleted successfully"}