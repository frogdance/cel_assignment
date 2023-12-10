from pydantic import BaseModel

class SaleReport(BaseModel):
    item_identifier: str
    outlet_identifier: str
    item_visibility: float
    item_mrp: float
    item_outlet_sales: float