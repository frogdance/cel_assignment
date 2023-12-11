from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Annotated

from routers import get_db
from db.models import Item
from db.schemas import ItemSchema

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[ItemSchema])
async def get_items(
        db: Session = Depends(get_db),
        item_identifier: Annotated[list[str] | None, Query(title='the id of item to get')] = None,
        item_weight_min: Annotated[float | None, Query(title='min weight of item')] = None,
        item_weight_max: Annotated[float | None, Query(title='max weight of item')] = None,
        item_fat_content: Annotated[list[str] | None, Query(title='list of content of items (low fat or regular)')] = None,
        item_type: Annotated[list[str] | None, Query(title='list of category of items')] = None,
    ) -> list[ItemSchema]:
    """Return a list of all items
    """
    query = db.query(Item)

    # Apply filters based on the provided parameters
    if item_identifier:
        query = query.filter(Item.item_identifier.in_(item_identifier))

    if item_weight_min is not None:
        query = query.filter(Item.item_weight >= item_weight_min)

    if item_weight_max is not None:
        query = query.filter(Item.item_weight <= item_weight_max)

    if item_fat_content:
        query = query.filter(Item.item_fat_content.in_(item_fat_content))

    if item_type:
        query = query.filter(Item.item_type.in_(item_type))

    # Execute the query and return the results
    result = query.all()
    return result
