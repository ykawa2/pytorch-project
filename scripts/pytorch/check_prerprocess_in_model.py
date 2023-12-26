import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms


class Resize(nn.Module):
    def __init__(self, size):
        super(Resize, self).__init__()
        self.size = size

    def forward(self, x):
        return F.interpolate(x, size=self.size)


class NetWithNNModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        self.resize = Resize((224, 224))
        self.fc1 = nn.Linear(10, 1)

    def forward(self, x):
        out = self.normalize(x)
        out = self.resize(x)
        out = self.fc1(x)
        return out


class NetWithFunction(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 1)

    def forward(self, x):
        out = F.interpolate(x, size=(224, 224))
        out = F.normalize(x, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        out = self.fc1(x)
        return out


nn_module_model = NetWithNNModule()
print(nn_module_model)

function_model = NetWithFunction()
print(function_model)
