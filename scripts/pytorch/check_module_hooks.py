import torch
import torch.nn as nn


class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc = nn.Linear(10, 5)  # 例としての線形層

    def forward(self, x):
        return self.fc(x)


# モデルのインスタンスを作成
model = MyModel()


# 前処理フック（入力の形状を表示）
def forward_pre_hook(module, input):
    print("Input Shape:", input[0].shape)


# 後処理フック（出力の形状を表示）
def forward_hook(module, input, output):
    print("Output Shape:", output.shape)


# フックをモデルに追加
model.register_forward_pre_hook(forward_pre_hook)
model.register_forward_hook(forward_hook)

# テスト入力
input = torch.randn(1, 10)  # ランダムな入力テンソル

# モデルを通して入力を渡す
output = model(input)

print(output)
# Input Shape: torch.Size([1, 10])
# Output Shape: torch.Size([1, 5])
# tensor([[-0.5214,  0.7575, -0.8372, -1.0827,  0.4365]],
#        grad_fn=<AddmmBackward0>)
