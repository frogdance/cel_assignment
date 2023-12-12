from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Annotated

from routers import get_db
from db.models import Outlet
from db.schemas import OutletSchema

router = APIRouter(
    prefix="/outlets",
    tags=["outlets"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[OutletSchema])
async def get_items(
        db: Session = Depends(get_db),
        outlet_identifier: Annotated[list[str] | None, Query(title='the id of outlet to get')] = None,
        outlet_establishment_year: Annotated[list[int] | None, Query(title='min weight of outlet')] = None,
        outlet_size: Annotated[list[str] | None, Query(title='max weight of outlet')] = None,
        outlet_location_type: Annotated[list[str] | None, Query(title='list of content of outlets (low fat or regular)')] = None,
        outlet_type: Annotated[list[str] | None, Query(title='list of category of outlets')] = None,
    ) -> list[OutletSchema]:
    """
    Query Outlet.

    Parameters:
    - outlet_identifier: List string of outlet id.
    - outlet_establishment_year: List integer of year establish.
    - outlet_size: List string of outlet size.
    - outlet_location_type: List string of outlet location type.
    - outlet_type: List string of outlet type.

    Returns:
    list of Outlet.
    """
    query = db.query(Outlet)

    # Apply filters based on the provided parameters
    if outlet_identifier:
        query = query.filter(Outlet.outlet_identifier.in_(outlet_identifier))

    if outlet_establishment_year is not None:
        query = query.filter(Outlet.outlet_establishment_year.in_(outlet_establishment_year))

    if outlet_size is not None:
        query = query.filter(Outlet.outlet_size.in_(outlet_size))

    if outlet_location_type:
        query = query.filter(Outlet.outlet_location_type.in_(outlet_location_type))

    if outlet_type:
        query = query.filter(Outlet.outlet_type.in_(outlet_type))

    # Execute the query and return the results
    result = query.all()
    return result
