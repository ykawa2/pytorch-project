import torch
import torch.nn as nn


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(10, 10)

    def forward(self, x):
        return self.fc(x)


model = Net()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

output = model(torch.randn(10, 10))
loss = output.sum()
loss.backward()

parameters = list(model.parameters())
state_dict = model.state_dict()

optimizer.zero_grad()

print(parameters)
print(state_dict)
