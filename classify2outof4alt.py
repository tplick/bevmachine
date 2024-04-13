#!/usr/bin/env python3

from bevmachine import BevCMachine

m = BevCMachine(1.001)
m.bind((0, 0, 0, 0), 0)
m.bind((1, 0, 0, 0), 0)
m.bind((0, 1, 0, 0), 0)
m.bind((0, 0, 1, 0), 0)
m.bind((0, 0, 0, 1), 0)
m.bind((1, 1, 0, 0), 1)
m.bind((1, 0, 1, 0), 1)
m.bind((0, 1, 1, 0), 1)
m.bind((1, 0, 0, 1), 1)
m.bind((0, 1, 0, 1), 1)
m.bind((0, 0, 1, 1), 1)
m.demo()

