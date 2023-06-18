from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# @app.get('/')
# async def root():
#     return {"message":"Hello World"}
#
# @app.post('/')
# async def post():
#     return {"message": "Hello from post router"}

@app.get("/items")
async def list():
    return {"message": "list"}


@app.get("/items/{item_id}")
async def detail_(item_id: str):
    return {"item_id": item_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}
    if food_name.value == "fruits":
        return {"food_name": food_name, "message": "you are more healthy"}
    return {"food_name": food_name, "message": "Im diary"}
