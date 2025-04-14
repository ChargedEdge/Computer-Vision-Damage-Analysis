import kagglehub
from app.download.datasets import move_dataset
from app.definitions import MODEL_MATERIAL_DIR, CONCRETE_DAMAGE_DIR

def download_concrete_dataset():
    path = kagglehub.dataset_download("arnavr10880/concrete-crack-images-for-classification")

    concrete_normal_download_path = f"{path}/Negative"
    concrete_crack_download_path = f"{path}/Positive"

    move_dataset(concrete_normal_download_path, MODEL_MATERIAL_DIR, "concrete")
    move_dataset(concrete_crack_download_path, CONCRETE_DAMAGE_DIR, "cracked")

