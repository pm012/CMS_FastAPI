from typing import List, Optional
from datetime import date, timedelta

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactBase, ContactUpdate


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactBase, db: Session) -> Contact:    
    contact = Contact(name=body.name, surname = body.surname, email = body.email, phone = body.phone, birth_date = body.birth_date, additional_data = body.additional_data)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        if body.name is not None:
            contact.name = body.name
        if body.surname is not None:
            contact.surname = body.surname
        if body.email is not None:
            contact.email = body.email
        if body.phone is not None:
            contact.phone = body.phone
        if body.birth_date is not None:
            contact.birth_date = body.birth_date
        if body.additional_data is not None:
            contact.additional_data = body.additional_data
        db.commit()
        db.refresh(contact)
    return contact

async def search_contacts(name: Optional[str], surname: Optional[str], email: Optional[str], db: Session) -> List[Contact]:
    query = db.query(Contact)
    if name:
        query = query.filter(Contact.name.ilike(f"%{name}%"))
    if surname:
        query = query.filter(Contact.surname.ilike(f"%{surname}%"))
    if email:
        query = query.filter(Contact.email.ilike(f"%{email}%"))
    return query.all()

async def get_upcoming_birthdays(db: Session) -> List[Contact]:
    today = date.today()
    next_week = today + timedelta(days=7)
    return db.query(Contact).filter(Contact.birth_date.between(today, next_week)).all()
