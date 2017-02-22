import numpy as np
from math import factorial


def _sin(x):
    val = np.float64(0)
    terms = np.array([], dtype=np.float64)
    for n in range(41):
        term = (((-1) ** n) * (x ** (2*n+1)) / factorial(2*n + 1))
        terms = np.append(terms, term)
        val += term
    return val, terms

def debug_sin(x):
    val, terms = _sin(x)
    tmp = np.float64(0)
    for i, t in enumerate(terms):
        tmp += t
        print("for x_{0}, term is {1}, sin({2}) approximation is {3}".format(
            i, t, x, tmp))
    return val

def sin(x):
    v, _ = _sin(x)
    return v

def cos(x):
    val = np.float64(0)
    for n in range(41):
        term = (((-1) ** n) * (x ** (2*n)) / factorial(2*n))
        val += term
    return val

pi = np.float64(22./7.)
print("pi is initially {0}".format(pi))
for i in range(5):
    pi += sin(pi)
    print("improving pi iteration {0}, pi: {1}".format(i, pi))

if __name__ == "__main__":
    vals = np.array([0, pi / 4., pi / 2., pi * 3./4., pi], dtype=np.float64)
    for n in vals:
        print("sin({0}) = {1}".format(n, sin(n)))
        print("cos({0}) = {1}".format(n, cos(n)))
