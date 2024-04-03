#!/usr/bin/env python3

from bevmachine import BevMachine

m = BevMachine(1.001)
m.bind((0, 0, 0, 0, 0), 0)
m.bind((1, 0, 0, 0, 0), 16)
m.bind((1, 1, 0, 0, 0), 16 + 8)
m.bind((1, 1, 1, 0, 0), 16 + 8 + 4)
m.bind((1, 1, 1, 1, 0), 16 + 8 + 4 + 2)
m.bind((1, 1, 1, 1, 1), 16 + 8 + 4 + 2 + 1)
m.demo()

