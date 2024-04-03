#!/usr/bin/env python3
# Learn 5 ^ (x1 + x2 + x3 + x4 + x5) from a single sample.
# This seems only to work when the base of the machine
# is also 5.

from bevmachine import BevMachine

m = BevMachine(5)
m.bind((1, 1, 1, 1, 1), 3125)
m.demo()

