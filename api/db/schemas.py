from pydantic import BaseModel

class ItemSchema(BaseModel):
    item_identifier: str
    item_weight: float
    item_fat_content: str
    item_type: str

class OutletSchema(BaseModel):
    outlet_identifier: str
    outlet_establishment_year: int
    outlet_size: str | None
    outlet_location_type: str
    outlet_type: str

class SaleReportSchema(BaseModel):
    item_identifier: str
    outlet_identifier: str
    item_visibility: float
    item_mrp: float
    item_outlet_sales: float