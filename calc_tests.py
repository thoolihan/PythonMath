import unittest
import numpy as np
import calculus as calc

class CalcTests(unittest.TestCase):
    def test_euler(self):
        x = np.pi / 4.
        y_est, ys, ds = calc.euler(dy_dx = lambda x,y: np.cos(x),
                                   y0 = 0,
                                   h = 1e-4,
                                   start = 0,
                                   end = x)
        self.assertAlmostEqual(y_est, np.sin(x), places = 3,
                               msg = "Estimate should be close to actual sin of value")

    def test_newton(self):
        fx = lambda x: -4*x**3 - 2*x**2 - 2*x - 3
        dx = lambda x: -12*x**2 - 4*x - 2
        x_n = calc.newton(iter = 10, x0 = -2, fx = fx, dx = dx)
        self.assertAlmostEqual(x_n[2], -1.058263, places = 4,
                               msg = "Estimate of root does not match answer")
