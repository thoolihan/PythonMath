"""
Calculus module
"""

import numpy as np

def euler(dy_dx = lambda x,y: None, h = 1e-3, y0 = 1, start = 0, end = 1):
    """
    Use Euler method to approximate value based on derivative.
    Params:
        dy_dx: a function that calculates the derivative based on x (and possibly y)
        h: step size to move towards end
        y0: y value when x is start
        start: first x value
        end: x value to approximate
    Returns:
        estimated y value,
        incremental y values as a list,
        incremental derivatives as a list

    Example:
    # Evaluate x**2 at 1 using Euler knowing only derivative and that 0**2 = 0
    y_vals = euler(lambda x, y: 2 * x, start = 0, y0 = 0, end = 1)
    print("1^2: %f euler pred: %f difference: %f" % (1**2, y_vals[-1], float(1**2) - y_vals[-1]))
    >>> 1^2: 1.000000 euler pred: 1.000001 difference: -0.000001
    """
    nsteps = float(end - start) / h
    ys = np.array([y0])
    ds = np.array([dy_dx(start-h, y0)])
    for i in range(int(nsteps) + 1):
        x = start + i * h
        dyx = dy_dx(x, ys[i])
        ds = np.append(ds, dyx)
        ys = np.append(ys, ys[i] + h * dyx)
    return (ys[-1], ys, ds)

def newton(iter = 10, x0 = 0., fx = lambda x: x, dx = lambda x: x):
    """
    Use Newton's method of finding a root (0) of a complex equation
    Params:
        iter: number of values to return
        x0: initial x value to start with
        fx: the function
        dx: the derivative
    Returns:
        x_vals: a numpy array of the xvalues it guessed
    Example:
        x_vals = newton(iter = 2,
                        x0 = 1
                        fx = lambda x: 5*x**3 - 5*x + 7,
                        dx = lambda x: 15*x**2 - 5)
        print(x_vals)
        >>>
    """
    x_vals = np.array([x0])
    for i in range(iter):
        x = x_vals[-1]
        x_vals = np.append(x_vals, x - (fx(x)/dx(x)))
    return x_vals

def mvt(a, b, fx = lambda x: x):
    """
    Mean value theorem
    Params:
        a: start of interval
        b: end of interval
        fx: function
    Returns:
        f_c: derivative of some point c that is a <= c <= b
    """
    return (fx(b) - fx(a))/(b - a)
