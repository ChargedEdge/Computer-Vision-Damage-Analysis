from fastapi import APIRouter, HTTPException
from uuid import UUID
from app.server.models.schemas import AnalysisResultResponse


router = APIRouter()



@router.get("/{id}", response_model=AnalysisResultResponse)
async def get_analysis_result(id: str):
    # TODO: Get results from the analysis
    data = None

    # Check if there is any data with id
    if not data:
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    # Check if the image is done processing
    if data["status"] != "done":
        raise HTTPException(status_code=202, detail="Still processing image.")
    
    # Return result of the analysis
    return data["result"]

