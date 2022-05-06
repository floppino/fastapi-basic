from pydantic import BaseModel, validator

"""
########################################################################################################################
                                             SCHEMA IN
########################################################################################################################
"""


class RatSchemaIn(BaseModel):
    rat_name: str
    rat_owner_name: str

    @validator("rat_name", "rat_owner_name", pre=True)
    def capitalize_name(cls, field: str):
        if field is not None:
            return field.capitalize()

    class Config:
        orm_mode = True


class RatSchemaOut(BaseModel):
    rat_id: int
    rat_name: str
    rat_owner_name: str

    class Config:
        orm_mode = True
