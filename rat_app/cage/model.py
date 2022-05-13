from sqlalchemy import Column, Integer, String, Float, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Cage(Base):
    __tablename__ = "cage"
    cage_id = Column(Integer, primary_key=True)
    model = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    bar_space = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    depth = Column(Float, nullable=True)
    width = Column(Float, nullable=True)
    __table_args__ = (UniqueConstraint(model, price),)
