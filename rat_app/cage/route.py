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
@router.get("", status_code=status.HTTP_200_OK, response_model=List[CageSchemaOut])
async def get_cages():

    try:
        cages = db.session.query(Cage).all()

    except SQLAlchemyError as sql_error:
        print(f"Error retrieving data: {sql_error}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if len(cages) < 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return cages


# Get a cage by id
@router.get("/{cage_id}", status_code=status.HTTP_200_OK, response_model=CageSchemaOut)
async def cage_by_id(cage_id: int):
    try:
        cage = db.session.query(Cage).filter(Cage.cage_id == cage_id).one()

    except NoResultFound:
        print(f"Cage with id: {cage_id} not found ")
        raise HTTPException(status_code=404, detail="Cage not found")

    except SQLAlchemyError:
        print("Error retrieving data")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return cage


# Add a new cage
@router.post("", status_code=status.HTTP_201_CREATED, response_model=CageSchemaOut)
async def add_cage(cage: CageSchemaIn):

    try:
        db_cage = Cage(**dict(cage))
        db.session.add(db_cage)
        db.session.commit()
        db.session.refresh(db_cage)

    except IntegrityError as integrity_error:
        print(f"Cage - Integrity error - \n {integrity_error}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Integrity Error, Duplicated Entry",
        )

    except SQLAlchemyError:
        print("Error retrieving data")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return db_cage

# Delete a cage
@router.delete("/{cage_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cage(cage_id: int):

    try:
        cage_to_delete = db.session.query(Cage).filter(Cage.cage_id == cage_id).one()
        db.session.delete(cage_to_delete)
        db.session.commit()

    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cage is not present")

    except SQLAlchemyError:
        print(f"Error: \n\n{SQLAlchemyError}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return


# Update cage
@router.put("/{cage_id}", status_code=status.HTTP_200_OK)
async def update_cage(cage_id: int, cage: CageUpdateSchema):

    try:
        db.session.query(Cage).filter(Cage.cage_id == cage_id).one()
        db.session.query(Cage).filter(Cage.cage_id == cage_id).update(cage)
        db.session.commit()

    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cage is not present")

    except StatementError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong information")

    except SQLAlchemyError:
        print(f"Error: \n\n{SQLAlchemyError}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return cage
