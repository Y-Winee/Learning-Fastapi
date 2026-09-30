
from fastapi import APIRouter, HTTPException, status

from .dependencies import ServiceDependency
from .schema.shipment import ShipmentCreate, ShipmentRead, ShipmentUpdate

router = APIRouter(prefix="/shipment", tags=['Shipment'])

@router.get("/", response_model=ShipmentRead)
async def get_shipment(id: int, service: ServiceDependency):
    shipment = await service.get(id)

    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Given id: {id} isn't found"
        )
    return shipment

@router.post("/", response_model=ShipmentRead)
async def create_shipment(form: ShipmentCreate, service: ServiceDependency):
    return await service.add(form)

@router.patch("/", response_model=ShipmentRead)
async def update_shipment(id: int, form: ShipmentUpdate, service: ServiceDependency):
    shipment = form.model_dump(exclude_none=True)

    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data provided to update",
        )
    return await service.update(id, shipment)

@router.delete("/")
async def delete_shipment(id: int, service: ServiceDependency) -> str:
    await service.delete(id)
    return f"Shippment with id : {id} has been successfully deleted"