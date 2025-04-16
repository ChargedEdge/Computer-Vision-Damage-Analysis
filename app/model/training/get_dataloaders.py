from torchvision import datasets, transforms
from torch.utils.data import Subset, DataLoader
import numpy as np

def get_partial_dataset(dataset, fraction=0.2, seed=42):
    np.random.seed(seed)
    indices = np.random.permutation(len(dataset))
    subset_size = int(len(dataset) * fraction)
    subset_indices = indices[:subset_size]
    return Subset(dataset, subset_indices)


def get_dataloaders(data_dir, batch_size=32, image_size=224):
    transform = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor()
    ])

    train_dataset_full = datasets.ImageFolder(root=f"{data_dir}/train", transform=transform)
    val_dataset_full = datasets.ImageFolder(root=f"{data_dir}/validation", transform=transform)

    # For testing
    train_dataset = get_partial_dataset(train_dataset_full)
    val_dataset = get_partial_dataset(val_dataset_full)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, val_loader
