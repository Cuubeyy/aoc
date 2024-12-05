import numpy as np
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)


class Ray:
    def __init__(self, px, py, pz, vx, vy, vz):
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz


ans = 0
coords = []
task = open("24.in").read().splitlines()
for line in task:
    a, b = line.split(" @ ")
    px, py, pz = a.split(", ")
    vx, vy, vz = b.split(", ")
    coords.append(Ray(px, py, pz, vx, vy, vz))

print(ans)
