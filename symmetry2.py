#!/usr/bin/env python3
# Attempt to classify vector as symmetric or asymmetric.
# A symmetric vector has x1=x6, x2=x5, and x3=x4.
# Notice that the symmetric vectors are all mapped to 1
# and the asymmetric vectors are mapped to 0 or less.
# The problem is too nonlinear for the machine to produce
# a 0-1 response.

from bevmachine import BevMachine

m = BevMachine()
m.bind((0, 0, 0, 0, 0, 0), 1j)

m.bind((1, 0, 0, 0, 0, 0), 1)
m.bind((0, 0, 0, 0, 0, 1), 1)
m.bind((1, 0, 0, 0, 0, 1), 1j)

m.bind((0, 1, 0, 0, 0, 0), 1)
m.bind((0, 0, 0, 0, 1, 0), 1)
m.bind((0, 1, 0, 0, 1, 0), 1j)

m.bind((0, 0, 1, 0, 0, 0), 1)
m.bind((0, 0, 0, 1, 0, 0), 1)
m.bind((0, 0, 1, 1, 0, 0), 1j)
m.demo()

