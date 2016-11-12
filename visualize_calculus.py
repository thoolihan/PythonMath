"""
Visualizations for Calculus function
"""
import calculus as calc
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.ion()

def v_newton(iter=10, x0=0, fx=lambda x: x, dx=lambda x: x, width=5.):
    x = np.linspace(x0 - width, x0 + width, 100)
    y = fx(x)
    x_n = calc.newton(iter, x0, fx, dx)
    y_n = fx(x_n)
    plt.plot(x, y, 'b--')
    plt.plot(x_n, y_n, 'ro')
    labels = ['x{0}'.format(n) for n in range(len(x_n))]
    for lbl, x, y in zip(labels, x_n, y_n):
        plt.annotate(lbl, xy=(x,y), xytext = (-10, 10),
                     textcoords='offset points', alpha=.5)
    plt.show()


if __name__ == "__main__":
    v_newton(5, 3, lambda x: x**2, lambda x: 2*x)
    input('Press any key to exit...')
