### Recipe API ###

from fastapi import APIRouter, Depends

from src.integartions.factory import LLMFactory
from src.routers.schema import RecipeSchema
from src.settings import Settings, get_settings

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={
        200: {"message": "Recipe generation started"},
        500: {"message": "LLM service is down"},
    },
)


@router.post("/")
async def recipes(
    recipe: RecipeSchema,
    settings: Settings = Depends(get_settings),
) -> dict:
    llm_factory = LLMFactory(settings)
    llm = llm_factory.create_llm(recipe.model)

    return {"llm": recipe.model, "result": llm.chat(recipe.ingredients_as_text)}
