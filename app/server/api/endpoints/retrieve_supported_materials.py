from fastapi import APIRouter
#from app.server.models.schemas import MaterialTypesListResponse, MaterialType
from app.server.models.schemas import MaterialID

from app.definitions import SUPPORTED_MATERIALS

from typing import List


router = APIRouter()


@router.get("/materials", response_model=List[MaterialID])
async def get_supported_materials():
    return SUPPORTED_MATERIALS

