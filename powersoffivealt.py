#!/usr/bin/env python3
# Try to learn 5 ^ (x1 + x2 + x3 + x4 + x5) from a single sample.
# As an experiment, I have changed the machine base from 5 to -5.
# Observe what happens to the predictions.

from bevmachine import BevMachine

m = BevMachine(-5)
m.bind((1, 1, 1, 1, 1), 3125)
m.demo()

