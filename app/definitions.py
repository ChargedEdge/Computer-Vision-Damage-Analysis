import os

# Constants
NUMBER_OF_EPOCHS = 5

# material and damage types
SUPPORTED_MATERIALS = [
    'wood',
    'carpet',
    'drywall'
]

SUPPORTED_MATERIAL_DAMAGES = {
    'wood': [ 'water', 'fire', 'structural' ],
    'carpet': ['water', 'fire'],
    'drywall': ['water', 'fire', 'structural']
}








# Directories
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Images
IMAGE_UPLOAD_DIR = os.path.join(ROOT_DIR, "images/uploads")

# Results
RESULTS_DIR = os.path.join(ROOT_DIR, "images/results")


# Separate Module Directories
MODEL_DIR = os.path.join(ROOT_DIR, "model")

DOWNLOAD_DIR = os.path.join(ROOT_DIR, "download")

MODEL_DATA_DIR = os.path.join(ROOT_DIR, "data")
MODEL_MATERIAL_DIR = os.path.join(MODEL_DATA_DIR, "material")
MODEL_DAMAGE_DIR = os.path.join(MODEL_DATA_DIR, "damage")


# specific material damages
CONCRETE_DAMAGE_DIR = os.path.join(MODEL_DAMAGE_DIR, "concrete")




# Model file name defaults
MATERIAL_CLASSIFIER_FILE_NAME = "material_classifier.pt"
#DAMAGE_CLASSIFIER_FILE_NAME = "damage_classifer.pt"
DAMAGE_CLASSIFIER_FILE_NAME = lambda material : f"damage_{material}_model.pt"
