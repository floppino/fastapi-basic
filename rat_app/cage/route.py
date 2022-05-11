from typing import List
from fastapi import APIRouter, HTTPException, status, Security
from fastapi.responses import Response
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, StatementError
from sqlalchemy.orm.exc import NoResultFound
from rat_app.cage.model import Cage
from rat_app.cage.schema import CageSchemaIn, CageSchemaOut, CageUpdateSchema


# Instantiate Router
router = APIRouter()


# Get all cages
@router.get("", status_code=status.HTTP_200_OK, response_model=List[CageSchemaIn])
async def get_cages():

    try:
        cages = db.session.query(Cage).all()

    except SQLAlchemyError as sql_error:
        print(f"Error retrieving data: {sql_error}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if len(cages) < 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return cages


# Add a new cage
@router.post("/add_cage", status_code=status.HTTP_200_OK, response_model=CageSchemaOut)
async def add_cage(cage: CageSchemaIn):

    try:
        db_cage = Cage(**dict(cage))
        db.session.add(db_cage)
        db.session.commit()
        db.session.refresh(db_cage)

    except SQLAlchemyError:
        print("Error retrieving data")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return db_cage
