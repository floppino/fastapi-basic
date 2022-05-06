from typing import List

from fastapi import APIRouter, HTTPException, status, Security
from fastapi.responses import Response
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, StatementError
from sqlalchemy.orm.exc import NoResultFound


# Class import
from rat_app.rat.model import Rat
# Schema import
from rat_app.rat.schema import (
    #RatUpdateSchema,
    RatSchemaIn,
    RatSchemaOut
)

"""
########################################################################################################################
                                             ROUTE CONFIG
########################################################################################################################
"""

# Instantiate Router
router = APIRouter()

"""
########################################################################################################################
                                            Asset Entity Routes
########################################################################################################################
"""


# Get every rat
@router.get("", status_code=status.HTTP_200_OK, response_model=List[RatSchemaIn])
async def all_rats():
    """Return every rat"""
    try:
        rats = db.session.query(Rat).all()
    except SQLAlchemyError as sql_error:
        print(f"Error retrieving data: {sql_error}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if len(rats) < 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return rats


# Get a specific asset
@router.get("/{rat_id}", status_code=status.HTTP_200_OK, response_model=RatSchemaOut)
async def rat_by_id(rat_id: int):

    try:
        rat = db.session.query(Rat).filter(Rat.rat_id == rat_id).one()

    except NoResultFound:
        print(f"Rat with id: {rat_id} not found ")
        raise HTTPException(status_code=404, detail="Asset not found")
    except SQLAlchemyError:
        print("Error retrieving data")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return rat