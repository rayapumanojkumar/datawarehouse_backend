# app/main.py

from fastapi import FastAPI
from app.api.endpoints import webhook, data, sync, tasks

app = FastAPI()

app.include_router(webhook.router, prefix="/webhook", tags=["webhook"])
app.include_router(data.router, prefix="/data", tags=["data"])
app.include_router(sync.router, prefix="/sync", tags=["sync"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])


@app.get('/')
def healthy():
    return {
        "status": "healthy",
        "message": "Application is up and running"
    }