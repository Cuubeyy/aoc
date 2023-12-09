from datetime import datetime
import os
from aocd import get_data
import math

start = datetime.now()
task = open("input.txt").read().splitlines()
ans = 0


def add_layer(layers_):
    temp = []
    for i, number in enumerate(layers[-1][:-1]):
        temp.append(layers[-1][i + 1] - number)
    layers_.append(temp)
    return layers_


for line in task:
    layers = []
    numbers = list(map(int, line.split()))
    layers.append(numbers)
    while not all(v == 0 for v in layers[-1]):
        layers = add_layer(layers)

    last = 0
    for i, layer in enumerate(reversed(layers)):
        if i == 0:
            layer.insert(0, 0)
            continue
        last = layer[0] - last
        layer.insert(0, last)
    ans += last

print(ans)
print(datetime.now() - start)

