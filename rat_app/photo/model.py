from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    LargeBinary
)
from sqlalchemy.ext.declarative import declarative_base
from rat_app.rat.model import Rat
from sqlalchemy_imageattach.entity import Image


Base = declarative_base()


class Photo(Base, Image):
    __tablename__ = "photo"
    photo_id = Column(Integer, autoincrement=True)
    rat_photo = Column(String, primary_key=True)
    rat_id = Column(Integer, ForeignKey(Rat.rat_id))


