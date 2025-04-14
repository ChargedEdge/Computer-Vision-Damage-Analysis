from fastapi import APIRouter, HTTPException, UploadFile, File
from PIL import Image
from uuid import uuid4
from app.server.models.schemas import AnalysisSubmissionResponse


router = APIRouter()

@router.post("/analyse", response_model=AnalysisSubmissionResponse)
async def analyse_material(file: UploadFile = File(...)):
    id = uuid4()

    # Save image
    try:
        with Image.open(file) as img:
            if img.format not in ['PNG', "JPEG"]:
                raise HTTPException(status_code=404, detail="Unsupported file type. Only PNG and JPEG are allowed.")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file.")

    # TODO: Store image for later use    



    # TODO: Start image processing in background


    return AnalysisSubmissionResponse(id=id)

