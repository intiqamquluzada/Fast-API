from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

# @app.get('/')
# async def root():
#     return {"message":"Hello World"}
#
# @app.post('/')
# async def post():
#     return {"message": "Hello from post router"}

# @app.get("/items")
# async def list():
#     return {"message": "list"}
#
#
# @app.get("/items/{item_id}")
# async def detail_(item_id: str):
#     return {"item_id": item_id}
#
#
# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"
#
#
# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy"}
#     if food_name.value == "fruits":
#         return {"food_name": food_name, "message": "you are more healthy"}
#     return {"food_name": food_name, "message": "Im diary"}


fake_items_db = [
    {"item_name": "alma"},
    {"item_name": "armud"},
    {"item_name": "nar"},

]


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}

    if q:
        item.update({"q":q})

    if not short:
        item.update({"description": "loremloremloremloremlorem"})
    return item

