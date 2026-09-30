import datetime
from enum import Enum

from sqlmodel import Field, SQLModel


class ShippingStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"

class Shipment(SQLModel, table=True):
    __tablename__ = "shipment"

    id : int = Field(default=None, primary_key=True)
    content: str
    weight: float = Field(le=10, gt=0)
    destination: int
    status: ShippingStatus
    estimated_delivery: datetime.datetime