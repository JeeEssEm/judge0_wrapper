from fastapi import APIRouter, Request, Depends
from dishka.integrations.fastapi import DishkaRoute, FromDishka

from auth import require_login, bearer_schema
from services import Judge0Service
from schemas import CreateSubmissionSchema

router = APIRouter(prefix="/submissions", tags=["submissions"], route_class=DishkaRoute)


@router.get("/{submission_id}", dependencies=[Depends(bearer_schema)])
@require_login()
async def get_submission(submission_id: str, request: Request, judge_service: FromDishka[Judge0Service]):
    return await judge_service.get_submission(submission_id)


@router.post("/", dependencies=[Depends(bearer_schema)])
@require_login()
async def create_submission(
        submission: CreateSubmissionSchema,
        request: Request,
        judge_service: FromDishka[Judge0Service]
):
    # TODO: когда содержание задач будет лежать в бд этого сервиса, expected_result будет подставляться на бэкенде
    submission_token = await judge_service.create_submission(submission)
    return submission_token
