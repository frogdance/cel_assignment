from fastapi import APIRouter
import pandas as pd 

from .utils import connection
from models.outlet import Outlet

router = APIRouter(
    prefix="/outlets",
    tags=["outlets"],
    responses={404: {"description": "Not found"}},
)


@router.get("/",)
async def get_all_outlet() -> list[Outlet]:
    return pd.read_sql_query("select * from outlet", con=connection).to_dict('records')

@router.get("/{outlet_id}")
async def get_outlet(outlet_id: str) -> list[Outlet]:
    print(pd.read_sql_query(f"select * from outlet where outlet_identifier='{outlet_id}'", con=connection).to_dict('records'))
    return pd.read_sql_query(f"select * from outlet where outlet_identifier='{outlet_id}'", con=connection).to_dict('records')