import torch
import torch.nn as nn


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 1)

    def forward(self, x):
        out = self.fc1(x)
        return out


model = Net()
model_scripted = torch.jit.script(model)
model_scripted.save("/tmp/model.pt")
print(model_scripted)

# load
model = torch.jit.load("/tmp/model.pt")
print(model)
