import torch
import torch.nn as nn


class Mysoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        return x_exp/torch.sum(x_exp)


class SoftmaxStable (nn. Module):
    def __init__(self):
        super(). __init__()

    def forward(self, x):
        x_max = torch .max(x, dim=0, keepdims=True)
        x_exp = torch .exp(x - x_max . values)
        partition = x_exp .sum(0, keepdims=True)
        return x_exp / partition


data = torch.Tensor([1, 2, 3])
softmax = Mysoftmax()
softmax_stable = SoftmaxStable()
output1 = softmax(data)
output2 = softmax_stable(data)

print(output1)
print(output2)
