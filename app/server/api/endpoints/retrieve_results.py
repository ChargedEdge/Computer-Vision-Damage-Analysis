from fastapi import APIRouter, HTTPException
from uuid import UUID
from pathlib import Path
import json

from app.definitions import RESULTS_DIR
from app.server.models.schemas import AnalysisResultResponse


router = APIRouter()

results_dir = Path(RESULTS_DIR)
results_dir.mkdir(parents=True, exist_ok=True)

@router.get("/{id}", response_model=AnalysisResultResponse)
async def get_analysis_result(id: str):
    # Get results from the analysis
    results_path = RESULTS_DIR / f"{id}.json"

    # Check if there is any data with id
    if not results_path.exists():
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    try:
        with results_path.open('r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Corrupted result file")

    
    # Check if the image is done processing
    if data["status"] != "done":
        raise HTTPException(status_code=202, detail="Still processing image.")
    
    # Return result of the analysis
    return data

