import torch

x1 = torch.ones(5)
print(x1)

x2 = x1.data.numpy()
print(x2)

x3 = x1.numpy()
print(x3)
