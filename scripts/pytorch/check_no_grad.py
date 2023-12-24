import torch
import torch.nn as nn


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(10, 10)

    def forward(self, x):
        return self.fc(x)


model = Net()

output = model(torch.randn(10, 10))
loss = output.sum()
loss.backward()

with torch.no_grad():
    for param in model.parameters():
        param -= 0.1 * param.grad
print(model.parameters())

# Exception has occurred: RuntimeError
# a leaf Variable that requires grad is being used in an in-place operation.
#   File "/home/docker/pytorch-project/notebooks/scripts/check_no_grad.py", line 26, in <module>
#     param -= 0.1 * param.grad
# RuntimeError: a leaf Variable that requires grad is being used in an in-place operation.
for param in model.parameters():
    param -= 0.1 * param.grad
