from typing import List
from fastapi import APIRouter, HTTPException, status, Security
from fastapi.responses import Response
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, StatementError
from sqlalchemy.orm.exc import NoResultFound
from fastapi import UploadFile


# Class import
from rat_app.photo.model import Photo
# Schema import
from rat_app.photo.schema import (PhotoUpdateSchema, PhotoSchemaIn, PhotoSchemaOut)

"""
#Add a photo
@router.post("", status_code=status.HTTP_201_CREATED, response_model=PhotoSchemaOut)
async def add_photo(photo: UploadFile = PhotoSchemaIn):
    return photo
"""