from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from sqlalchemy.ext.asyncio import AsyncSession

from ..api.schema.shipment import ShipmentCreate, ShipmentUpdate
from ..database.model import Shipment, ShippingStatus


class ShipmentService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: int) -> Shipment:
        return await self.session.get(Shipment, id)

    async def add(self, shipment: ShipmentCreate) -> Shipment:
        new_shipment = Shipment(
            **shipment.model_dump(),
            status=ShippingStatus.placed,
            estimated_delivery=datetime.now(ZoneInfo("Asia/Rangoon")) + timedelta(days=3)
        )
        self.session.add(new_shipment)
        await self.session.commit()
        await self.session.refresh(new_shipment)
        return new_shipment

    async def update(self, id: int, form: ShipmentUpdate) -> Shipment:
        shipment = await self.get(id)
        if shipment is None:
            return None
        
        # If passing a dict from router:
        for key, value in form.items():
            setattr(shipment, key, value)

        self.session.add(shipment)
        await self.session.commit()
        await self.session.refresh(shipment)
        return shipment

    async def delete(self, id: int) -> bool:
        shipment = await self.get(id)
        if shipment is None:
            return False
        await self.session.delete(shipment)
        await self.session.commit()
        return True
        