#!/usr/bin/env python3

import random
import sys

from bevmachine import BevMachine

def f(v):
    return sum(4 ** sum(v[i:i+2]) for i in range(0, 20, 2))


m = BevMachine(1.001)

samples = int(sys.argv[1])
for _ in range(samples):
    vector = [random.choice([0, 1]) for i in range(20)]
    m.bind(vector, f(vector))

m.demo()

