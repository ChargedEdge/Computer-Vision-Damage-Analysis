from fastapi import APIRouter
from app.models.schemas import DamageTypesListResponse, DamageType

router = APIRouter()


@router.get("/types", response_model=DamageTypesListResponse)
async def get_supported_types():
    # TODO: Put accepted damage types here
    types = [
        DamageType(id="water", name="Water")
    ]

    return { "damage_types": types }
