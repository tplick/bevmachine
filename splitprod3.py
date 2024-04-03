#!/usr/bin/env python3
# Learn (x1 + x2) * (x3 + x4) * (x5 + x6) from a small set
# of examples.

from bevmachine import BevMachine

m = BevMachine(1.001)
m.bind((0, 0, 0, 0, 0, 0), 0)

m.bind((1, 1, 0, 0, 0, 0), 0)
m.bind((0, 0, 1, 1, 0, 0), 0)
m.bind((0, 0, 0, 0, 1, 1), 0)

m.bind((1, 1, 1, 1, 0, 0), 0)
m.bind((0, 0, 1, 1, 1, 1), 0)
m.bind((1, 1, 0, 0, 1, 1), 0)

m.bind((1, 1, 1, 1, 1, 1), 8)
m.demo()

