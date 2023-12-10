from pydantic import BaseModel

class Outlet(BaseModel):
    outlet_identifier: str
    outlet_establishment_year: int
    outlet_size: str | None
    outlet_location_type: str
    outlet_type: str