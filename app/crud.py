from sqlalchemy.orm import Session
from .models import Customer, Campaign
from .schemas import CustomerCreate, CampaignCreate


def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Customer).offset(skip).limit(limit).all()


def get_campaigns(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Campaign).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def create_campaign(db: Session, campaign: CampaignCreate):
    db_campaign = Campaign(**campaign.dict())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign
