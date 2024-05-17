from typing import List

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
        contact.name=body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.phone = body.phone
        contact.birth_date = body.birth_date
        contact.additional_data = body.additional_data        
        db.commit()
    return contact