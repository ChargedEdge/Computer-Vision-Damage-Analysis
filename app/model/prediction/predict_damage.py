import torch


def predict_damage(model, image_tensor, threshold=0.5, device='cpu'):
    model.eval()
    model.to(device)
    image_tensor = image_tensor.to(device)

    with torch.no_grad():
        probs = model(image_tensor).squeeze()
        predicted_indices = (probs > threshold).nonzero(as_tuple=True)[0].tolist()

    return predicted_indices

