import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import math
from PIL import Image


# loads the image into array with one channel
img = np.asarray(Image.open('data/simon.png', mode='r').convert('L'))
# Copies image data to fx and fy
fx = img.copy()
fy = img.copy()

imgStink = img.copy()

dim = (375, 500)

# Defines arrays of pixel sizes
# fx = np.zeros(dim)
# fy = np.zeros(dim)
def f(x, y):
    return 2 * x ** 2 - 3 * x * y + 4 * y ** 2

def f_x(f, x, y, dx):
    return (f(x + dx, y) - f(x - dx, y)) / (2 * dx)

def f_y(f, x, y, dy):
    return (f(y + dy, x) - f(y - dy, x)) / (2 * dy)

def f_discrete(img):
    diffx = img
    diffy = img
    diff = np.zeros(np.shape(img))

    for x in range(img.shape[0] - 1):
        for y in range(img.shape[1] - 1):
            diffx[x][y] = (img[x + 1][y + 1] - img[x][y]) / 2

    for y in range(img.shape[1] - 1):
        for x in range(img.shape[0] - 1):
            diffy[x][y] = (img[x + 1][y + 1] - img[x][y]) / 2

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            diff[y][y] = abs(np.sqrt((diffx[x][y]) ** 2 + (diffy[x][y]) ** 2))

    return diff

# Finds derivative of f for x
for iy, ix in np.ndindex(fx.shape):
    fx[iy][ix] = f_x(f, ix, iy, 1)

# Finds derivative of f for y
for iy, ix in np.ndindex(fy.shape):
    fy[iy][ix] = f_y(f, ix, iy, 1)

# Finds the length of the gradient
fgradabs = np.zeros(dim)
for iy, ix in np.ndindex(fgradabs.shape):
    fgradabs[iy][ix] = abs(np.sqrt((fx[iy][ix]) ** 2 + (fy[iy][ix]) ** 2))

# Find max and min
maxval = fgradabs.max()
minval = fgradabs.min()
fgradabs = np.interp(fgradabs,(minval,maxval),(0,1))

# Uncomment to use stinkbug
# Find max and min
maxval = imgStink.max()
minval = imgStink.min()

fgradabs = np.interp(imgStink,(minval,maxval),(0,1))


# Function to cut the pixels depending on the pixel stength
def kutt(x):
    c = 0.2
    for ix, iy in np.ndindex(x.shape):
        if x[ix][iy] <= c:
            x[ix][iy] = 0.0
        else:
            x[ix][iy] = 1.0
    return x

# imgplot = plt.imshow(fgradabs, cmap='Greys')
fgradabs = kutt(fgradabs)
imgplot = plt.imshow(fgradabs, cmap='Greys')

plt.show()
