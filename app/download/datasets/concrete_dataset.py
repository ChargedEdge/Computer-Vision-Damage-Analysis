import kagglehub
from app.download.datasets import move_dataset
from app.definitions import MODEL_DATA_DIR

def download_concrete_dataset():
    path = kagglehub.dataset_download("arnavr10880/concrete-crack-images-for-classification")

    print(f"Path to concrete dataset files: ${path}")

    concrete_normal_download_path = f"{path}/Negative"
    concrete_crack_download_path = f"{path}/Positive"

    move_dataset(concrete_normal_download_path, MODEL_DATA_DIR, "concrete_normal")
    move_dataset(concrete_crack_download_path, MODEL_DATA_DIR, "concrete_cracked")


