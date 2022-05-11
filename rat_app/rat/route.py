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
    RatUpdateSchema,
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
@router.get("", status_code=status.HTTP_200_OK, response_model=List[RatSchemaOut])
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


# Add a rat
@router.post("", status_code=status.HTTP_201_CREATED, response_model=RatSchemaOut)
async def add_rat(rat: RatSchemaIn):

    try:
        db_rat = Rat(**dict(rat))
        db.session.add(db_rat)
        db.session.commit()
        db.session.refresh(db_rat)

    except IntegrityError as integrity_error:
        print(f"Rat - Integrity error - \n {integrity_error}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Integrity Error, Duplicated Entry",
        )
    except SQLAlchemyError:
        print("Error retrieving data")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return db_rat


# Delete a rat
@router.delete("/{rat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rat(rat_id: int):

    try:
        rat_to_delete = db.session.query(Rat).filter(Rat.rat_id == rat_id).one()
        db.session.delete(rat_to_delete)
        db.session.commit()

    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rat is not present")

    except SQLAlchemyError:
        print(f"Error: \n\n{SQLAlchemyError}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return


# Update rat
@router.put("/{rat_id}", status_code=status.HTTP_200_OK)
async def update_rat(rat_id: int, rat: RatUpdateSchema):

    try:
        db.session.query(Rat).filter(Rat.rat_id == rat_id).one()
        db.session.query(Rat).filter(Rat.rat_id == rat_id).update(rat)
        db.session.commit()

    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rat is not present")

    except StatementError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong information")

    except SQLAlchemyError:
        print(f"Error: \n\n{SQLAlchemyError}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return rat




