from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Owner(Base):
    __tablename__ = "owner"
    owner_id = Column(Integer, primary_key=True)
    owner_name = Column(String(100), nullable=False)
    owner_email = Column(String(100), nullable=False)
