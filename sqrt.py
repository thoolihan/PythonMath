import numpy as np
import math

def sqrt(n, estimate, epsilon = 1e-15):
    error = math.fabs(n - (estimate ** 2))
    if error <= epsilon:
        print("error: {0}, returning {1}".format(error, estimate))
        return estimate
    else:
        print("error: {0}, recursing".format(error))
        estimate = (estimate + n / estimate) / 2.
        return sqrt(n, estimate, epsilon)

if __name__ == "__main__":
    print("np.sqrt(2): {0}".format(np.sqrt(2)))
    print("sqrt of 2 is: {0}".format(sqrt(2, 1.4)))


