from torch import nn, sigmoid
from torchvision import models

class MaterialDamageClassifier(nn.Module):
    def __init__(self, num_labels):
        super().__init__()
        self.model = models.resnet18(pretrained=True)
        self.model.fc = nn.Linear(self.model.fc.in_features, num_labels)

    def forward(self, x):
        return sigmoid(self.model(x))
