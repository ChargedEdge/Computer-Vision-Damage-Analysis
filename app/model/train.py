
from app.definitions import MODEL_MATERIAL_DIR, MODEL_DAMAGE_DIR, SUPPORTED_MATERIALS, SUPPORTED_MATERIAL_DAMAGES
from app.model.classifier import MaterialClassifier, MaterialDamageClassifier
from app.model.training import get_dataloaders, train_material_classifier, train_damage_classifier


# Train material classifier
material_train_loader, material_val_loader = get_dataloaders(MODEL_MATERIAL_DIR, batch_size=32)
print(f"Number of material classes: {len(SUPPORTED_MATERIALS)}")

material_model = MaterialClassifier(num_classes=len(SUPPORTED_MATERIALS))
train_material_classifier(material_model, material_train_loader, material_val_loader)


# Train material damage classifiers
for material, damage_labels in SUPPORTED_MATERIAL_DAMAGES.items():
    damage_train_loader, damage_val_loader = get_dataloaders(f"{MODEL_DAMAGE_DIR}/damage/{material}", batch_size=32)
    damage_model = MaterialDamageClassifier(num_labels=len(damage_labels))
    train_damage_classifier(material, damage_model, damage_train_loader, damage_val_loader)



