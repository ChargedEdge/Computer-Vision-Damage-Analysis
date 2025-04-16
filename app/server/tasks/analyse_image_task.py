from pathlib import Path

from app.definitions import RESULTS_DIR
from app.model import infer


results_dir = Path(RESULTS_DIR)
results_dir.mkdir(parents=True, exist_ok=True)

def analyse_image_task(image_path: str):
    print(f"Processing {image_path} in background")
