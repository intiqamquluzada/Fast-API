from fastapi import FastAPI, Query, Path
from enum import Enum
from typing import Optional
from pydantic import BaseModel

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


# @app.get("/items")
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}

    if q:
        item.update({"q": q})

    if not short:
        item.update({"description": "loremloremloregfrfgmloremlorem"})
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "loremloremloregfrfgmloremlorem"})
    return item


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_With_tax": price_with_tax})
#     return item_dict


@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})

    return result


@app.get("/items")
async def list_items(q: Optional[list[str]] = Query(None)):
    result = {}
    if q:
        result.update({"q": q})
    return result


@app.get("/items_hidden")
async def get_hidden_items(hidden_query: Optional[str] = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}

@app.get("/items_validation/{item_id}")
async def read_items_validation(q: Optional[str],item_id: int = Path(...,gt=10, lt=100), size: Optional[float] = Query(..., gt=1, lt=7.76)):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q":q})
    return results

print('demo')