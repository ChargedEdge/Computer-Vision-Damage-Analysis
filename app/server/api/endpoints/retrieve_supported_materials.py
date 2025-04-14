from fastapi import APIRouter
from app.server.models.schemas import MaterialTypesListResponse, MaterialType

router = APIRouter()


@router.get("/materials", response_model=MaterialTypesListResponse)
async def get_supported_materials():
    # TODO: Put accepted material types here
    materials = [
        MaterialType(id="wood", name="Wood")
    ]

    return { "materials": materials }

