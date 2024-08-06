# app/api/endpoints/tasks.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
def list_tasks():
    return {"message": "Listing all running background tasks"}


@router.post("/tasks/cancel")
def cancel_task(task_id: int):
    return {"message": f"Cancelling task {task_id}"}
