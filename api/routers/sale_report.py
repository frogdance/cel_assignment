from fastapi import APIRouter
import pandas as pd 

from .utils import connection
from models.sale_report import SaleReport

router = APIRouter(
    prefix="/sale_reports",
    tags=["sale_reports"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_sale_report() -> list[SaleReport]:
    return pd.read_sql_query("select * from sale_report", con=connection).to_dict('records')

