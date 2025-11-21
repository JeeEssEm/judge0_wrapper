from fastapi import APIRouter

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from services import Judge0Service

router = APIRouter(tags=["information"], route_class=DishkaRoute)


@router.get("/languages")
async def get_languages(
        service: FromDishka[Judge0Service],
) -> list[dict]:
    return await service.get_available_languages()
