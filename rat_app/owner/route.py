from typing import List
from fastapi import APIRouter, HTTPException, status, Security
from fastapi.responses import Response
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, StatementError
from sqlalchemy.orm.exc import NoResultFound
from rat_app.owner.model import Owner
from rat_app.owner.schema import OwnerSchemaIn, OwnerSchemaOut, OwnerUpdateSchema


# Instantiate Router
router = APIRouter()


# Get all owners
@router.get("", status_code=status.HTTP_200_OK, response_model=List[OwnerSchemaIn])
async def get_owners():

    try:
        owners = db.session.query(Owner).all()

    except SQLAlchemyError as sql_error:
        print(f"Error retrieving data: {sql_error}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if len(owners) < 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return owners


# Add a new owner
@router.post("", status_code=status.HTTP_200_OK, response_model=OwnerSchemaOut)
async def add_owner(owner: OwnerSchemaIn):

    try:
        db_owner = Owner(**dict(owner))
        db.session.add(db_owner)
        db.session.commit()
        db.session.refresh(db_owner)

    except SQLAlchemyError:
        print("Error retrieving data")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return db_owner
