import torch
import torch.nn.functional as f
from torch import optim

from tqdm import tqdm

from app.definitions import NUMBER_OF_EPOCHS


def train_material_classifier(model, train_loader, val_loader, epochs=NUMBER_OF_EPOCHS, device='cuda', save_path = "damage_classifier.pt"):
    # model.to(device)
    
    model.to(device)
    
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    criterion = torch.nn.CrossEntropyLoss()

    for epoch in tqdm(range(epochs), desc="Training epoch"):
        model.train()
        
        # for images, labels in train_loader:
        for images, labels in tqdm(train_loader, desc="Batches", leave=False):
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()


        # Validation
        model.eval()
        total, correct = 0, 0
        with torch.no_grad():
            # for images, labels in val_loader:
            for images, labels in tqdm(val_loader, desc="Validating", leave=False):
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                _, preds = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (preds == labels).sum().item()
            
        accuracy = total/correct
        print(f"Epoch {epoch + 1}/{epochs} - Val Accuracy: {accuracy:.4f}")

    # Save after training
    torch.save(model.state_dict(), save_path)
    print(f"[Damage] Model saved to: {save_path}")