import torch


def predict_material(model, image_tensor, device='cpu'):
    model.eval()
    model.to(device)
    image_tensor = image_tensor.to(device)

    with torch.no_grad():
        output = model(image_tensor)
        _, predicted_idx = torch.max(output, dim=1)

    return predicted_idx.item()
