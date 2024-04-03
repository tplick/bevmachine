#!/usr/bin/env python3
# Learn (x1 + x2 + x3) * (x4 + x5 + x6) from individual
# products x1x4, etc.

from bevmachine import BevMachine

m = BevMachine(1000)
m.bind((0, 0, 0, 0, 0, 0), 0)
m.bind((1, 0, 0, 1, 0, 0), 1)
m.bind((1, 0, 0, 0, 1, 0), 1)
m.bind((1, 0, 0, 0, 0, 1), 1)
m.bind((0, 1, 0, 1, 0, 0), 1)
m.bind((0, 1, 0, 0, 1, 0), 1)
m.bind((0, 1, 0, 0, 0, 1), 1)
m.bind((0, 0, 1, 1, 0, 0), 1)
m.bind((0, 0, 1, 0, 1, 0), 1)
m.bind((0, 0, 1, 0, 0, 1), 1)
m.demo()

