from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from rat_app.owner.model import Owner


Base = declarative_base()


class Rat(Base):
    __tablename__ = "rat"
    rat_id = Column(Integer, primary_key=True)
    rat_name = Column(String(100), nullable=False, unique=True)
    owner_id = Column(Integer, ForeignKey(Owner.owner_id))
    __table_args__ = (UniqueConstraint(rat_name, owner_id),)
