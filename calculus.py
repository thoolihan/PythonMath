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
    """

    nsteps = float(end - start) / h
    ys = [y0]
    for i in range(int(nsteps) + 1):
        x = start + i * h
        ys.append(ys[i] + h * dy_dx(x, ys[i]))
    return ys
