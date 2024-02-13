import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

dx = 0.01
def f(x, y):
    return 8*x+y**2


def f_x(f, x, y, dx):
    return (f(x+dx, y) - f(x-dx, y)) / (2*dx)

# OPPGAVE 1a.
# image with effects
fx = np.zeros((375, 500))
for iy, ix in np.ndindex(fx.shape):
    fx[iy][ix] = f_x(f, ix, iy, dx)

plt.matshow(fx)





