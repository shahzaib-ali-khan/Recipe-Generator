from fastapi import FastAPI

from routers import recipe, supported_llm

app = FastAPI()


app.include_router(recipe.router)
app.include_router(supported_llm.router)
