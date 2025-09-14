# Contacts management system on  FastAPI

## Instructions

1. Activate environment and install rquirements.txt:
   `pip install -r requirements.txt`
2. Launch Postgres database:
   `docker-compose up -d`
3. Generate data to the DBMS:
   `python /src/database/populate_db.py`
4. Run the following command to start server:
   `uvicorn main:app --host localhost --port 8000 --reload`
5. To view generated documents and try requirests open http://localhost:8000/docs in browser

## Task

The purpose of this project is to create an REST API for storing and managing contacts. The API should be built using FastAPI infrastructure and use SQLALchemy to manage the database.

-[x] Contacts should be stored in the database and contain the following information:
_ Name
_ Last Name
_ E-address
_ Phone number
_ Birthday
_ Additional data (optional)

-[x] The API should be able to perform the following actions:
_ Create a new contact
_ Get a list of all contacts
_ Get one contact by ID
_ Update existing contact \* Delete Contact

-[x] In addition to the basic functionality of the CRUD API should also have the following functions:
_ Contacts should be available for search by name, surname or email address.
_ The API should be able to get a list of contacts with birthdays for the next 7 days.

## General requirements

1. Using FastAPI framework to create API
2. Using ORM SQLALchemy to work with database (model is done using sqlalchemy)
3. PostgreSQL should be used as a database (implemented with docker-compose).
4. Support CRUD operations for contacts (implemented)
5. Support for storing birth date contact (datebirth is stored, for some reason API returns datetime with zero time mark)
6. Providing documents for API (generated automatically by FastAPI, see instructions above)
7. Using the Pydantic data reliability verification module (implemented in schemas.py)
