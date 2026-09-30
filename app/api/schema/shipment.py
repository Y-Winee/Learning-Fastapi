from datetime import datetime

from pydantic import BaseModel, Field

from ...database.model import ShippingStatus


class BaseShipment(BaseModel):
    content: str
    weight: float = Field(le=10, gt=0)
    destination: int

class ShipmentRead(BaseShipment):
    id: int
    status: ShippingStatus
    estimated_delivery: datetime

class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseShipment):
    status: ShippingStatus | None = Field(default=None)
    estimated_delivery: datetime | None = Field(default=None)