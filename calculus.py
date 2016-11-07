"""
Calculus module
"""

def euler(dy_dx = lambda x,y: None, h = 1e-6, y0 = 1, start = 0, end = 1):
    """
    Use Euler method to approximate value based on derivative.
    dy_dx: a function that calculates the derivative based on x (and possibly y)
    h: step size to move towards end
    y0: y value when x is start
    start: first x value
    end: x value to approximate

    Example:
    # Evaluate x**2 at 1 using Euler knowing only derivative and that 0**2 = 0
    y_vals = euler(lambda x, y: 2 * x, start = 0, y0 = 0, end = 1)
    print("1^2: %f euler pred: %f difference: %f" % (1**2, y_vals[-1], float(1**2) - y_vals[-1]))
    >>> 1^2: 1.000000 euler pred: 1.000001 difference: -0.000001
    """

    nsteps = float(end - start) / h
    ys = [y0]
    for i in range(int(nsteps) + 1):
        x = start + i * h
        ys.append(ys[i] + h * dy_dx(x, ys[i]))
    return ys
