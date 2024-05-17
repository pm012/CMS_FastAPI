from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    email = Column(String(80), nullable=False)
    phone = Column(String(20), nullable=False)
    birth_date = Column('birth_date', DateTime, nullable=False)
    additional_data = Column(String(150))
