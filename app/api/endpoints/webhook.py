# app/api/endpoints/webhook.py

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import SessionLocal
from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/webhook", response_model=schemas.Customer)
def receive_webhook(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.create_customer(db, customer=customer)
    return db_customer


# app/api/endpoints/webhook.py

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import SessionLocal
from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/webhook", response_model=schemas.Customer)
def receive_webhook(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.create_customer(db, customer=customer)
    return db_customer
