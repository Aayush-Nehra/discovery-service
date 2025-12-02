from pydantic import BaseModel, Field
from datetime import datetime


class ServiceBase(BaseModel):
    name: str = Field(..., max_length=200)
    category: str = Field(..., max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    latitude: float
    longitude: float


class ServiceCreate(ServiceBase):
    owner_id: int | None = None


class ServiceUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    description: str | None = None
    latitude: float | None = None
    longitude: float | None = None


class ServiceInDBase(ServiceBase):
    id: int
    owner_id: int | None = None
    created_at: datetime

    class Config:
        from_attributes = True


class ServiceResponse(ServiceInDBase):
    pass
