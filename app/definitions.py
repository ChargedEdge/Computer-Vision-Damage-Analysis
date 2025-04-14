import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Separate Module Directories
MODEL_DIR = os.path.join(ROOT_DIR, "model")

DOWNLOAD_DIR = os.path.join(ROOT_DIR, "download")

MODEL_DATA_DIR = os.path.join(ROOT_DIR, "data")
MODEL_MATERIAL_DIR = os.path.join(MODEL_DATA_DIR, "material")
MODEL_DAMAGE_DIR = os.path.join(MODEL_DATA_DIR, "damage")


# specific material damages
CONCRETE_DAMAGE_DIR = os.path.join(MODEL_DAMAGE_DIR, "concrete")




