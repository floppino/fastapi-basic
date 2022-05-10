from pydantic import BaseModel, validator
from typing import Optional


class OwnerSchemaIn(BaseModel):
    owner_name: str
    owner_email: str

    @validator("owner_name", pre=True)
    def capitalize_name(cls, field: str):
        if field is not None:
            return field.capitalize()

    class Config:
        orm_mode = True


class OwnerSchemaOut(BaseModel):
    owner_id: int
    owner_name: str
    owner_email: str

    class Config:
        orm_mode = True


class OwnerUpdateSchema(BaseModel):
    owner_name: Optional[str]
    owner_email: Optional[str]

    class Config:
        orm_mode = True