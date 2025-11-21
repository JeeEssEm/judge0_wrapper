from fastapi import APIRouter, Request, Depends

from dishka.integrations.fastapi import DishkaRoute, FromDishka

from auth import bearer_schema, require_login

router = APIRouter(prefix="/tasks", tags=["tasks"], route_class=DishkaRoute)


@router.get("/{task_id}", dependencies=[Depends(bearer_schema)])
@require_login()
async def get_task_info(task_id: int, request: Request):
    user = request.state.user
    print(user)
    return {}  # пока что не храним сами задачи
