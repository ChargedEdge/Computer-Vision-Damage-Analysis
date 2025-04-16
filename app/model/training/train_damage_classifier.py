import torch
import torch.nn.functional as F
from torch import optim

from tqdm import tqdm

from app.definitions import NUMBER_OF_EPOCHS


def train_damage_classifier(model, train_loader, val_loader, epochs = NUMBER_OF_EPOCHS, device = 'cuda', save_path="material_classifer.pt"):
    model.to(device)

    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    criterion = torch.nn.BCELoss()

    for epoch in range(epochs):
        model.train()
        
        for images, labels, in tqdm(train_loader, desc="Damage Batches", leave=False):
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()


        # Validation
        model.eval()
        total_loss = 0
        with torch.no_grad():
            for iamges, labels in val_loader:
                images, labels = images.to(device), labels.float().to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                total_loss += loss.item()

        print(f"Epoch {epoch + 1}/{epochs} - Val Loss: {total_loss:.4f}")

    # Save after training
    torch.save(model.state_dict(), save_path)
    print(f"[Damage] Model saved to: {save_path}")


