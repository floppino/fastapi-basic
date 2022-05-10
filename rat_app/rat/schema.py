from pydantic import BaseModel, validator
from typing import Optional

"""
########################################################################################################################
                                             SCHEMA IN
########################################################################################################################
"""


class RatSchemaIn(BaseModel):
    rat_name: str
    owner_id: int

    @validator("rat_name", pre=True)
    def capitalize_name(cls, field: str):
        if field is not None:
            return field.capitalize()

    class Config:
        orm_mode = True


class RatSchemaOut(BaseModel):
    rat_id: int
    rat_name: str
    owner_id: int

    class Config:
        orm_mode = True


class RatUpdateSchema(BaseModel):
    rat_name: Optional[str]
    owner_id: Optional[int]

    class Config:
        orm_mode = True