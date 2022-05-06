from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Rat(Base):
    __tablename__ = "rat"
    rat_id = Column(Integer, primary_key=True)
    rat_name = Column(String(100), nullable=False)
    rat_owner_name = Column(String(200), nullable=True)
