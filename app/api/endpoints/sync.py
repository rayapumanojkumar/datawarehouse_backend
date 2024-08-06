# app/api/endpoints/sync.py
import os
import httpx
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import SessionLocal

router = APIRouter()

CRM_API_URL = os.environ.get("CRM_API_URL")
MARKETING_API_URL = os.environ.get("MARKETING_API_URL")
API_KEY = os.environ.get("API_KEY")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def sync_crm_data(db: Session):
    async with httpx.AsyncClient() as client:
        response = await client.get(CRM_API_URL, headers={"X-API-Key": API_KEY})
        if response.status_code == 200:
            customers = response.json()
            for customer in customers:
                db_customer = schemas.CustomerCreate(**customer)
                crud.create_customer(db, customer=db_customer)


async def sync_marketing_data(db: Session):
    async with httpx.AsyncClient() as client:
        response = await client.get(MARKETING_API_URL, headers={"X-API-Key": API_KEY})
        if response.status_code == 200:
            campaigns = response.json()
            for campaign in campaigns:
                db_campaign = schemas.CampaignCreate(**campaign)
                crud.create_campaign(db, campaign=db_campaign)


@router.get("/sync/{source}")
async def sync_data(source: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    if source == "crm":
        background_tasks.add_task(sync_crm_data, db)
    elif source == "marketing":
        background_tasks.add_task(sync_marketing_data, db)
    else:
        raise HTTPException(status_code=400, detail="Invalid data source")
    return {"message": f"Syncing {source} data in the background"}
