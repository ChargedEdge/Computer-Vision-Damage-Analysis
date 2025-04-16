import torch

from app.model.prediction import load_image, predict_material, predict_damage
from app.model.classifier import MaterialClassifier, MaterialDamageClassifier

from app.definitions import SUPPORTED_MATERIALS, SUPPORTED_MATERIAL_DAMAGES, MATERIAL_CLASSIFIER_FILE_NAME, DAMAGE_CLASSIFIER_FILE_NAME


def infer(image_path, device='cpu'):
    # Load and preprocess the image
    image_tensor = load_image(image_path=image_path)

    # Load material classifier
    material_model = MaterialClassifier(num_classes=len(SUPPORTED_MATERIALS))
    material_model.load_state_dict(torch.load(MATERIAL_CLASSIFIER_FILE_NAME, map_location=device))

    # Predict material
    material_idx = predict_material(model=material_model, image_tensor=image_tensor, device=device)
    material = SUPPORTED_MATERIALS[material_idx]
    print(f"Predicted material: {material}")

    # Load corresponding damage classifier
    damage_labels = SUPPORTED_MATERIAL_DAMAGES[material]
    damage_model = MaterialDamageClassifier(num_labels=len(damage_labels))
    damage_model.load_state_dict(torch.load(DAMAGE_CLASSIFIER_FILE_NAME(material), map_location=device))

    # Predict damage types
    damage_indices = predict_damage(model=damage_model, image_tensor=image_tensor, device=device)
    damages = [damage_labels[i] for i in damage_indices]

    print(f"Detected damage types: {damages}")

    return { material, damages }


