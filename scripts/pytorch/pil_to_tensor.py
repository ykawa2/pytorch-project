import numpy as np
import torch
from PIL import Image

img = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
pil_img = Image.fromarray(img)

img = np.array(pil_img)
img_tensor = torch.as_tensor(img)
print(img_tensor.dtype)  # torch.uint8
