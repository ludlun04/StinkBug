import sys
from datetime import datetime

import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import math
from PIL import Image

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

# Oppgave 1c
# Lengde av gradienten
def f_gradlen(dx, dy):
    diff = np.zeros(dx.shape)
    for iy, ix in np.ndindex(dx.shape):
        diff[iy][ix] = np.sqrt((dx[iy][ix]) ** 2 + (dy[iy][ix]) ** 2)
    return diff

def g_smoothing(nabla_f, lambdaValue):
    return 1 / (np.sqrt(1 + (np.square(nabla_f) / (lambdaValue ** 2))))














# DET ER FEIL I KODEN. SYNTAX (ikke syntax som gir bort boller og kaffe kun på onsdager💀💀💀) ERROR.
def syntax(kaffe, boller):
    day = datetime.datetime.today().weekday()
    if (day == "wednesday"):
        return kaffe + boller
    sys.exit()