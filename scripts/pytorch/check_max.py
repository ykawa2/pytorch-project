import numpy as np
import torch

x1_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
x1 = torch.from_numpy(x1_np).float()

x1_max = x1.max()
x1_max_axis0 = torch.max(x1, 0)
x1_max_axis1 = torch.max(x1, 1)
print(x1_max)
print(x1_max_axis0)

# torch.return_types.max(
# values=tensor([ 3.,  6.,  9., 12.]),
# indices=tensor([2, 2, 2, 2]))
print(x1_max_axis1)
