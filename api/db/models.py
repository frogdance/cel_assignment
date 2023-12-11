from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .db import Base


class Item(Base):
    __tablename__ = "item"

    item_identifier = Column(String, primary_key=True)
    item_weight = Column(Float)
    item_fat_content = Column(String)
    item_type = Column(String)

class Outlet(Base):
    __tablename__ = "outlet"

    outlet_identifier = Column(String, primary_key=True)
    outlet_establishment_year = Column(Integer)
    outlet_size = Column(String)
    outlet_location_type = Column(String)
    outlet_type = Column(String)

class SaleReport(Base):
    __tablename__ = "sale_report"
    id = Column(Integer, primary_key=True)
    item_identifier = Column(String, ForeignKey('item.item_identifier'))
    outlet_identifier = Column(String, ForeignKey('outlet.outlet_identifier'))
    item_visibility = Column(Float)
    item_mrp = Column(Float)
    item_outlet_sales = Column(Float)