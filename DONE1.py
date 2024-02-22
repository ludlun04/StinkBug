import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import math
from PIL import Image


# loads the image into array with one channel
img = np.asarray(Image.open('data/image001.png', mode='r').convert('L'))
# Copies image data to fx and fy
img1 = img.copy()
img2 = img.copy()

dim = np.shape(img)
c = 0.4 #0.45 rimelig verdi

# Oppgave 1a
# Derivert ved x
def f_discrete_x(img):
    diff = img
    for ix, iy in np.ndindex((img.shape[0] - 1, img.shape[1] - 1)):
        diff[ix][iy] = (img[ix+1][iy] - img[ix][iy]) / 2.0 #gange med delta?

    return diff

fx = f_discrete_x(img1)

# Oppgave 1b
# Derivert ved y
def f_discrete_y(mat):
    diff = mat
    for ix, iy in np.ndindex((mat.shape[0] - 1, mat.shape[1] - 1)):
        diff[ix][iy] = (mat[ix][iy+1] - mat[ix][iy]) / 2.0 #gange med delta?

    return diff

fy = f_discrete_y(img2)

# Oppgave 1c
# Lengde av gradienten
def f_gradlen(dx, dy):
    diff = np.zeros(dx.shape)
    for iy, ix in np.ndindex(dx.shape):
        diff[iy][ix] = np.sqrt((dx[iy][ix]) ** 2 + (dy[iy][ix]) ** 2)
    return diff

fgradabs = f_gradlen(fx, fy)

# Oppgave 1 d.
maxval = fgradabs.max()
minval = fgradabs.min()
fgradabs = np.interp(fgradabs,(minval,maxval),(0,1))

# Oppgave 1f
def kutt(x, tolerance):
    for ix, iy in np.ndindex(x.shape):
        if x[ix][iy] <= tolerance:
            x[ix][iy] = 0.0
        else:
            x[ix][iy] = 1.0
    return x

fgradabs = kutt(fgradabs, c)

imgplot = plt.imshow(fgradabs, cmap='gist_gray')

plt.show()