### Recipe API ###

from fastapi import APIRouter

from src.integartions.factory import LLMFactory

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={
        200: {"message": "Recipe generation started"},
        500: {"message": "LLM service is down"},
    },
)


@router.get("/")
async def recipes(selected_model: str, ingrediants_as_text: str) -> dict:
    llm = LLMFactory.create_llm(selected_model)
    return {"llm": selected_model, "response": llm.chat(ingrediants_as_text)}
