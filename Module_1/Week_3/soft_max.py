import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self,x):
        x_exp=torch.exp(x)
        total = x_exp.sum(0, keepdims=True)
        return x_exp/total



#test
softmax=Softmax()
data=torch.Tensor([1,2,3])
output=softmax(data)
print(output)
        