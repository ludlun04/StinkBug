import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import math
from PIL import Image


# loads the image into array with one channel
img = np.asarray(Image.open('data/image001.png', mode='r').convert('L'))
# Copies image data to fx and fy


dim = np.shape(img)
c = 0.1 #0.45 rimelig verdi

# Oppgave 1a
# Derivert ved x
def f_discrete_x(img):
    new = np.zeros_like(img)
    for ix, iy in np.ndindex((new.shape[0] - 1, new.shape[1] - 1)):
        if ix == 0 or iy == 0:
            continue
        new[ix][iy] = (img[ix+1][iy] - img[ix-1][iy]) / 2.0 #gange med delta?

    return new

# Oppgave 1b
# Derivert ved y
def f_discrete_y(img):
    new = np.zeros_like(img)
    for ix, iy in np.ndindex((new.shape[0] - 1, new.shape[1] - 1)):
        if ix == 0 or iy == 0:
            continue
        new[ix][iy] = (img[ix][iy+1] - img[ix][iy-1]) / 2.0 #gange med delta?

    return new

# Oppgave 1f
def kutt(x, tolerance):
    for ix, iy in np.ndindex(x.shape):
        if x[ix][iy] <= tolerance:
            x[ix][iy] = 0.0
        else:
            x[ix][iy] = 1.0
    return x


t = 40
deltaT = .1

blurred = np.copy(img).astype('float64')



for i in range(t):
    fx = f_discrete_y(blurred)
    fy = f_discrete_y(blurred)
    fxx = f_discrete_x(fx)
    fyy = f_discrete_y(fy)

    blurred += deltaT * (fxx + fyy)
    print("iteration", i+1)

    if (i%10 == 0):
        plt.imshow(blurred, cmap='pink')
        plt.show()
print("done")





img1 = blurred.copy()
img2 = blurred.copy()

fx = f_discrete_x(img1)



fy = f_discrete_y(img2)

# Oppgave 1c
# Lengde av gradienten
def f_gradlen(dx, dy):
    diff = np.zeros(dx.shape)
    for iy, ix in np.ndindex(dx.shape):
        diff[iy][ix] = np.sqrt((dx[iy][ix]) ** 2 + (dy[iy][ix]) ** 2)
    return diff

fgradabs = f_gradlen(fx, fy)

maxval = fgradabs.max()
minval = fgradabs.min()
fgradabs = np.interp(fgradabs,(minval,maxval),(0,1))
fgradabs = kutt(fgradabs, c)
# Oppgave 1 d.
maxval = fgradabs.max()
minval = fgradabs.min()
# fgradabs = np.interp(fgradabs,(minval,maxval),(0,1))



# fgradabs = kutt(fgradabs, c)



imgplot = plt.imshow(fgradabs, cmap='gist_gray')

plt.show()