from fastapi import APIRouter, Path, Body
from typing import Annotated
import pandas as pd 

from .utils import connection
from models.item import Item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_all_items() -> list[Item]:
    """Return a list of all items
    """
    return pd.read_sql_query("select * from item", con=connection).to_dict('records')

@router.get("/{item_id}")
async def get_item(
    item_id: Annotated[str, Path(title='the id of item to get')]
) -> list[Item]:
    """Return a list of an item by item_id
    """
    return pd.read_sql_query(f"select * from item where item_identifier='{item_id}'", con=connection).to_dict('records')

@router.get("/get_items")
async def get_items(
    item_id: Annotated[list[str] | None, Body(title='the id of item to get')],
    item_weight_min: Annotated[float | None, Body(title='min weight of item')],
    item_weight_max: Annotated[float | None, Body(title='max weight of item')],
    item_fat_content: Annotated[list[str] | None, Body(title='list of content of items (low fat or regular)')],
    item_type: Annotated[list[str] | None, Body(title='list of category of items')],
) -> list[Item]:
    """Return a list of item by given filter parameters
    """
    query = "select * from item"

    if item_id and item_weight_min and item_weight_max and item_fat_content and item_type != None:
        query += 'where'
        # item id
        if item_id != None:
            query += f"item_id IN {set(item_id)}"
        # item_weight_min
        if item_weight_min and item_weight_max != None:


    return pd.read_sql_query(query, con=connection).to_dict('records')