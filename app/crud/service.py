from sqlalchemy.orm import Session
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate


def create_service(db: Session, data: ServiceCreate) -> Service:
    obj = Service(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_service(db: Session, service_id: int) -> Service | None:
    return db.query(Service).filter(Service.id == service_id).first()


def list_service(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Service).offset(skip).limit(limit).all()


def update_service(db: Session, db_obj: Service, data: ServiceUpdate) -> Service:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def delete_service(db: Session, service_id: int):
    obj = get_service(db, service_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj
