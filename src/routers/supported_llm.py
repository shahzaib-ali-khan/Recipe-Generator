### Static conf API ###

from fastapi import APIRouter, Depends

from src.settings import Settings, get_settings

router = APIRouter(
    prefix="/supported_llms",
    tags=["Supported LLMs"],
    responses={
        200: {"message": "List of LLms"},
    },
)


@router.get("/")
async def supported_llms(settings: Settings = Depends(get_settings)):
    return settings.supported_llms
