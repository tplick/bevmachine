#!/usr/bin/env python3

import random
import sys

from bevmachine import BevMachine

def f(v):
    return sum(v * 2**(9-i) for i, v in enumerate(v))


m = BevMachine(1.001)

samples = int(sys.argv[1])
for _ in range(samples):
    vector = [random.choice([0, 1]) for i in range(10)]
    m.bind(vector, f(vector))

m.demo()

