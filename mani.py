import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
from PIL import Image
# How to solve the oppgave: https://matplotlib.org/stable/tutorials/images.html

dx = 1 #
dimensions = (375, 500)
img = np.asarray(Image.open('data/image001.png', mode='r').convert('L'))
imgStink = img.copy()
def f(x, y):
    return x**2+y**2

def f_x(array, x, y, dx):
    print(y)
    return (array[y][x + dx] - array[y][x-dx]) / (2*dx)

# OPPGAVE 1a. :-)
# image with effects
for ix in range(img.shape[0] - 1):
    for iy in range(img.shape[1] - 1):
        imgStink[ix][iy] = f_x(imgStink, ix, iy, dx)

plt.matshow(imgStink)
plt.show()

# OPPGAVE 1b.
# image with effects
def f_y(f, x,y,dy):
    return (f(y+dy,x)-f(y-dy,x))/(2*dy)
fy = np.zeros(dimensions)
for iy, ix in np.ndindex(imgStink.shape):
    fy[iy][ix] = f_y(f, ix, iy, dx)


# OPPGAVE 1c.
fgradabs = np.zeros(dimensions)
for iy, ix in np.ndindex(fgradabs.shape):
    fgradabs[iy][ix] = np.sqrt((imgStink[iy][ix])**2 + (fy[iy][ix])**2)

# OPPGAVE 1d.


#plt.matshow(fgradabs)
#plt.show()


