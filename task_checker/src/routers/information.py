from fastapi import APIRouter

router = APIRouter(tags=["information"])


@router.get("/languages")
async def get_languages():
    ...

