from pydantic import BaseModel, validator
from typing import Optional


class CageSchemaIn(BaseModel):
    model: str
    price: float
    bar_space: float
    height: float
    depth: float
    width: float

    @validator("model", pre=True)
    def capitalize_name(cls, field: str):
        if field is not None:
            return field.capitalize()

    class Config:
        orm_mode = True


class CageSchemaOut(BaseModel):
    cage_id: int
    model: str
    price: float
    bar_space: float
    height: float
    depth: float
    width: float

    class Config:
        orm_mode = True


class CageUpdateSchema(BaseModel):
    model: Optional[float]
    price: Optional[float]
    bar_space: Optional[float]
    height: Optional[float]
    depth: Optional[float]
    width: Optional[float]

    class Config:
        orm_mode = True