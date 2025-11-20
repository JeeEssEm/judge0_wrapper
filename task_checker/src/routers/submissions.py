from fastapi import APIRouter

router = APIRouter(prefix="/tasks/{task_id}/submissions", tags=["submissions"])


@router.get("/{submission_id}")
async def get_submission(task_id: int, submission_id: int):
    return {}


@router.post("/")
async def create_submission():
    ...
