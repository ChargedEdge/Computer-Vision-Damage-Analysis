from fastapi import APIRouter
from app.server.models.schemas import DamageTypesListResponse, MaterialID

from app.definitions import SUPPORTED_MATERIAL_DAMAGES

from typing import List

router = APIRouter()


@router.get("/types", response_model=dict[MaterialID, List[str]])
async def get_supported_types():
    return SUPPORTED_MATERIAL_DAMAGES
