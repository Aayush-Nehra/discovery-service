from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse
from app.crud import service as service_crud

# Server-side:

# Use dependency to get current user (verify JWT or basic token).

# Validate coordinates: latitude between -90 and 90, longitude -180..180.

# Insert Service record with owner_id set to current user.

# Return 201 + created service resource.

# If you prefer to avoid JWT in Week 1: require email + password fields in the body and internally call crud.user.authenticate(email, password) — but be cautious: sending credentials every request is not ideal. JWT is easy: use pyjwt and short expiry.

router = APIRouter(prefix="/services", tags=["services"])

@router.post("/register_service/", response_model=ServiceResponse)
def create_service(data: ServiceCreate, db: Session = Depends(get_db)):
    # Use dependency to get current user (verify JWT or basic token).
    # Validate coordinates: latitude between -90 and 90, longitude -180..180.
    # Insert Service record with owner_id set to current user.
    # Return 201 + created service resource.
    service = service_crud.create_service(db, data)
    return service

#Minimal Scaffolding for other items update later
@router.get("/{service_id}", response_model=ServiceResponse)
def read_service(service_id: int, db: Session = Depends(get_db)):
    service = service_crud.get_service(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


@router.get("/", response_model=list[ServiceResponse])
def list_all_services(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return service_crud.list_services(db, skip, limit)


@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(service_id: int, data: ServiceUpdate, db: Session = Depends(get_db)):
    service = service_crud.get_service(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service_crud.update_service(db, service, data)


@router.delete("/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db)):
    service = service_crud.delete_service(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"detail": "Deleted successfully"}