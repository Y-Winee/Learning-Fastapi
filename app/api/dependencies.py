from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..database.session import get_session
from ..service.shipment_service import ShipmentService

SessionDependency = Annotated[
    AsyncSession, 
    Depends(get_session)
]

def get_service(session: SessionDependency):
    return ShipmentService(session=session)

ServiceDependency = Annotated[
    ShipmentService,
    Depends(get_service)
]