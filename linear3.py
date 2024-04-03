#!/usr/bin/env python3

from bevmachine import BevMachine

m = BevMachine(1.001)
m.bind((0, 0, 0, 0, 0), 0)
m.bind((0, 0, 0, 0, 1), 1)
m.bind((0, 0, 0, 1, 1), 1 + 2)
m.bind((0, 0, 1, 1, 1), 1 + 2 + 4)
m.bind((0, 1, 1, 1, 1), 1 + 2 + 4 + 8)
m.bind((1, 1, 1, 1, 1), 1 + 2 + 4 + 8 + 16)
m.demo()

