import torch

state_dict = torch.load("/home/docker/iter_130000.pth")
print(state_dict.keys())
