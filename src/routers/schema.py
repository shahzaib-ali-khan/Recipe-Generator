from pydantic import BaseModel


class RecipeSchema(BaseModel):
    model: str
    ingredients_as_text: str
