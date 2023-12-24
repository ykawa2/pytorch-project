import numpy as np
import torch

x1 = torch.tensor(1)  # torch.int64
x1 = x1.float()  # torch.float32
print(x1, x1.requires_grad)

x2 = torch.tensor(1.0)  # torch.float32
print(x2)

x3 = np.array([1])  # np.int64
x3 = torch.from_numpy(x3)  # torch.int64
x3 = x3.float()  # torch.float32
print(x3)

x4 = np.array([1.0])  # np.float64
x4 = torch.from_numpy(x4)  # torch.float64
x4 = x4.float()  # torch.float32
print(x4)
