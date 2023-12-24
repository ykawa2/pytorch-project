import torch
import torch.nn as nn


class SubNet(nn.Module):
    def __init__(self):
        super(SubNet, self).__init__()
        self.fc2 = nn.Linear(10, 2)

    def forward(self, x):
        return self.fc2(x)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(10, 10)
        self.subnet = SubNet()

    def forward(self, x):
        out = self.fc(x)
        out = self.subnet(out)
        return


layer1 = nn.Linear(2, 2)

params = layer1.parameters()  # <generator object Module.parameters>
params = list(params)
print(params)

named_params = layer1.named_parameters()  # <generator object Module.named_parameters>
named_params = list(named_params)
print(named_params)

print("=========================================")
# fc1.weight
# fc1.bias
# subnet.fc2.weight
# subnet.fc2.bias
model = Net()
for name, param in model.named_parameters():
    print(name, param)
