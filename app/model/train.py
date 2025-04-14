import torch
from torchvision import transforms
from PIL import Image
from .classifier import MaterialClassifier


NUMBER_OF_EPOCHS = 5

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")





# Material definitions and their damage types
material_classes = ["concrete"]

damage_label_map = {
    "concrete": ["cracked"],
    # ...
}




# TODO: Train the material classifier




# TODO: Train Damage Classifiers


