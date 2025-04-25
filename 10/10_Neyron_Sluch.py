# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 20:00:03 2024

@author: Admin
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class MyNetwork(nn.Module):
    def __init__(self):
        super(MyNetwork, self).__init__()
        self.fc1 = nn.Linear(20, 10)
        self.fc2 = nn.Linear(10, 5)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.log_softmax(self.fc2(x), dim=1)
        return x

def main():
    print("Neural network example")

    net = MyNetwork()

    input_data = torch.randn(1, 20)
    output_data = net(input_data)

    print("Input:", input_data)
    print("Output:", output_data)

if __name__ == "__main__":
    main()
