
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class ContactBase(BaseModel):
    name: str = Field(max_length=30)
    surname: str = Field(max_length=30)
    email: EmailStr
    phone: str = Field(max_length=20)
    birth_date: datetime    
    additional_data: Optional[str] = Field(max_length=150, default=None)


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    name: Optional[str] = Field(max_length=30, default=None)
    surname: Optional[str] = Field(max_length=30, default=None)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(max_length=20, default=None)
    birth_date: Optional[datetime] = None
    additional_data: Optional[str] = Field(max_length=150, default=None)


class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True

