from pydantic import BaseModel, HttpUrl
from typing import Optional

"""
########################################################################################################################
                                             SCHEMA IN
########################################################################################################################
"""


class PhotoSchemaIn(BaseModel):
    rat_photo: HttpUrl
    rat_id: int

    class Config:
        orm_mode = True


class PhotoSchemaOut(BaseModel):
    photo_id: int
    rat_photo: HttpUrl
    rat_id: int

    class Config:
        orm_mode = True


class PhotoUpdateSchema(BaseModel):
    rat_photo: Optional[HttpUrl]
    rat_id: Optional[int]

    class Config:
        orm_mode = True