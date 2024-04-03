#!/usr/bin/env python3
# Tom Plick
# created March 30, 2024

from itertools import product

import numpy as np

def bev_product(base, u, v):
    return base ** np.dot(u, v)


class BevMachine:
    def __init__(self, base=2.0):
        self.bindings = {}
        self.base = base

    def bind(self, input, output):
        input = tuple(input)
        self.bindings[input] = output

    def compute(self):
        A, w = [], []
        for input, output in self.bindings.items():
            A.append(input)
            w.append(output)

        B = np.matrix([[bev_product(self.base, u, v) for v in A] for u in A])

        self.support_vectors = A
        self.weights = B.I.dot(w)

    def predict(self, input):
        correlation_vector = [bev_product(self.base, input, v) for v in self.support_vectors]
        return np.dot(correlation_vector, np.transpose(self.weights))[0,0]

    def predict_all(self):
        n = len(next(self.bindings.__iter__()))
        for x in product(*([(0, 1)] * n)):
            print(f"{x} -> {self.predict(x)}")

    def show_bindings(self):
        for input, output in self.bindings.items():
            print(f"{input} -> {output}")

    def demo(self):
        self.compute()
        print(self.__dict__)
        print()
        print("Bindings:")
        self.show_bindings()
        print()
        print("All predictions:")
        self.predict_all()

