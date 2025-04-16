from fastapi import APIRouter, HTTPException, UploadFile, File, BackgroundTasks
from pathlib import Path
import shutil
from uuid import uuid4

# from app.server.models.schemas import AnalysisSubmissionResponse
from app.server.models import AnalysisSubmissionResponse, Results
from app.server.tasks import analyse_image_task
from app.definitions import IMAGE_UPLOAD_DIR, RESULTS_DIR

router = APIRouter()


upload_dir = Path(IMAGE_UPLOAD_DIR)
upload_dir.mkdir(parents=True, exist_ok=True)

results_dir = Path(RESULTS_DIR)
results_dir.mkdir(parents=True, exist_ok=True)


@router.post("/analyse", response_model=AnalysisSubmissionResponse)
async def analyse_material(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    id = uuid4()
    
    file_extension = Path(file.filename).suffix
    if file_extension not in ['PNG', 'JPEG']:
        raise HTTPException(status_code=404, detail="Unsupported file type. Only PNG and JPEG are allowed.")
    

    # Store image for later use    
    unique_file_name = f"{id}{file_extension}"
    file_path = upload_dir / unique_file_name

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


    # Start image processing in background
    background_tasks.add_task(analyse_image_task, str(file_path))


    # Create default results file
    results = Results(id)
    results_file_path = results_dir / f"{id}.json"
    
    with open(results_file_path, 'w') as f:
        f.write(results.to_json())
    

    return AnalysisSubmissionResponse(id=id)

