from pydantic import BaseModel

class Item(BaseModel):
    item_identifier: str
    item_weight: float
    item_fat_content: str
    item_type: str