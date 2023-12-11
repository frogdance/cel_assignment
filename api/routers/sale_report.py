from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Annotated

from routers import get_db
from db.models import SaleReport
from db.schemas import SaleReportSchema

router = APIRouter(
    prefix="/sale_reports",
    tags=["sale_reports"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[SaleReportSchema])
async def get_items(
        db: Session = Depends(get_db),
        item_identifier: Annotated[list[str] | None, Query(title='the id of item to get')] = None,
        outlet_identifier: Annotated[list[int] | None, Query(title='the id of outlet to get')] = None,
        item_visibility: Annotated[float | None, Query(title='percentage of product display on total store area')] = None,
        item_mrp: Annotated[float | None, Query(title='maximum retail price')] = None,
        item_outlet_sales: Annotated[float | None, Query(title='sale of product')] = None,
    ) -> list[SaleReportSchema]:
    """Return a list of all outlets
    """
    query = db.query(SaleReport)

    # Apply filters based on the provided parameters
    if item_identifier:
        query = query.filter(SaleReport.outlet_identifier.in_(outlet_identifier))

    if outlet_identifier is not None:
        query = query.filter(SaleReport.outlet_identifier.in_(outlet_identifier))

    if item_visibility is not None:
        query = query.filter(SaleReport.item_visibility >= item_visibility)

    if item_mrp:
        query = query.filter(SaleReport.item_mrp >= item_mrp)

    if item_outlet_sales:
        query = query.filter(SaleReport.item_outlet_sales >= item_outlet_sales)

    # Execute the query and return the results
    result = query.all()
    return result
