from pathlib import Path

from app.definitions import RESULTS_DIR
from app.server.models import Results
from app.model import infer


results_dir = Path(RESULTS_DIR)
results_dir.mkdir(parents=True, exist_ok=True)

def analyse_image_task(image_path: str):
    print(f"Processing {image_path} in background")

    # Run analysis on model
    material, damages = infer(image_path)


    # Save results to JSON
    id = Path(image_path).stem

    results = Results(id, material, damages)
    
    json_data = results.to_json()
    results_file_path = results_dir / f"{id}.json"

    with results_file_path.open('w') as f:
        f.write(json_data)

    print(f"Finished image {id} analysis")
    


