#!/usr/bin/env python3
# Learn 16 * x1 + 8 * x2 + 4 * x3 + 2 * x4 + x5, i.e., the
# value of (x1, x2, x3, x4, x5) interpreted as a binary number.

from bevmachine import BevMachine

m = BevMachine()
m.bind((0, 0, 0, 0, 0), 0)
m.bind((1, 0, 0, 0, 0), 16)
m.bind((0, 1, 0, 0, 0), 8)
m.bind((0, 0, 1, 0, 0), 4)
m.bind((0, 0, 0, 1, 0), 2)
m.bind((0, 0, 0, 0, 1), 1)
m.demo()

