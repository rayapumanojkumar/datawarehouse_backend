# app/schemas.py

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class CustomerBase(BaseModel):
    name: str
    email: str


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int

    class Config:
        from_attributes = True


class CampaignBase(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime


class CampaignCreate(CampaignBase):
    pass


class Campaign(CampaignBase):
    id: int

    class Config:
        from_attributes = True
