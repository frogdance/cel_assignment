from pydantic import BaseModel

class Item(BaseModel):
    item_identifier: str
    item_weight: float
    item_fat_content: str
    item_type: str

class Outlet(BaseModel):
    outlet_identifier: str
    outlet_establishment_year: int
    outlet_size: str
    outlet_location_Type: str
    outlet_type: str

class SaleReport(BaseModel):
    item_identifier: str
    outlet_identifier: str
    item_visibility: float
    item_mrp: float
    item_outlet_sales: float

