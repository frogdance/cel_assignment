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
        outlet_identifier: Annotated[list[str] | None, Query(title='the id of outlet to get')] = None,
        item_visibility_min: Annotated[float | None, Query(title='min percentage of product display on total store area')] = None,
        item_visibility_max: Annotated[float | None, Query(title='max percentage of product display on total store area')] = None,
        item_mrp_min: Annotated[float | None, Query(title='min retail price')] = None,
        item_mrp_max: Annotated[float | None, Query(title='max retail price')] = None,
        item_outlet_sales_min: Annotated[float | None, Query(title='min sale of product')] = None,
        item_outlet_sales_max: Annotated[float | None, Query(title='max sale of product')] = None,
    ) -> list[SaleReportSchema]:
    """
    Query Sale Report.

    Parameters:
    - item_identifier: List string of item id.
    - outlet_identifier: List string of outlet id.
    - item_visibility_min: Float of min item visibility.
    - item_visibility_max: Float of max item visibility.
    - item_mrp_min: Float of min item mrp.
    - item_mrp_max: Float of max item mrp.
    - item_outlet_sales_min: Float of min item outlet sales.
    - item_outlet_sales_max: Float of max item outlet sales.

    Returns:
    list of Sale Report.
    """
    query = db.query(SaleReport)

    # Apply filters based on the provided parameters
    if item_identifier is not None:
        query = query.filter(SaleReport.item_identifier.in_(item_identifier))

    if outlet_identifier is not None:
        query = query.filter(SaleReport.outlet_identifier.in_(outlet_identifier))

    if item_visibility_min is not None:
        query = query.filter(SaleReport.item_visibility >= item_visibility_min)

    if item_visibility_max is not None:
        query = query.filter(SaleReport.item_visibility <= item_visibility_max)

    if item_mrp_min is not None:
        query = query.filter(SaleReport.item_mrp >= item_mrp_min)

    if item_mrp_max is not None:
        query = query.filter(SaleReport.item_mrp <= item_mrp_max)

    if item_outlet_sales_min is not None:
        query = query.filter(SaleReport.item_outlet_sales >= item_outlet_sales_min)

    if item_outlet_sales_max is not None:
        query = query.filter(SaleReport.item_outlet_sales <= item_outlet_sales_max)

    # Execute the query and return the results
    result = query.all()
    return result
