
# Oppgave 1a
# Derivert ved x
def f_discrete_x(img):
    diff = img

    dsx = img.shape[0] - 1
    dsy = img.shape[1] - 1
    shape = np.ndindex((dsx, dsy))

    for ix, iy in shape:
        diff[ix][iy] = (img[ix+1][iy] - img[ix][iy]) / 2.0  # gange med delta?

    return diff


# Oppgave 1b
# Derivert ved y
def f_discrete_y(img):
    diff = img

    dsx = img.shape[0] - 1
    dsy = img.shape[1] - 1
    shape = np.ndindex((dsx, dsy))

    for ix, iy in shape:
        diff[ix][iy] = (img[ix][iy+1] - img[ix][iy]) / 2.0  # gange med delta?

    return diff


# Oppgave 1c
# Lengde av gradienten
def f_gradlen(dx, dy):
    diff = np.zeros(dx.shape)
    for iy, ix in np.ndindex(dx.shape):
        diff[iy][ix] = np.sqrt((dx[iy][ix]) ** 2 + (dy[iy][ix]) ** 2)
    return diff


# Oppgave 1f
def cut(x, tolerance):
    for ix, iy in np.ndindex(x.shape):
        if x[ix][iy] <= tolerance:
            x[ix][iy] = 0.0
        else:
            x[ix][iy] = 1.0
    return x


def main():
    # loads the image into array with one channel
    img = np.asarray(Image.open('data/image001.png', mode='r').convert('L'))

    # Copies image data to fx and fy
    img1 = img.copy()
    img2 = img.copy()

    c = 0.4  # 0.45 rimelig verdi
    fx = f_discrete_x(img1)
    fy = f_discrete_y(img2)
    fgradabs = f_gradlen(fx, fy)

    # Oppgave 1 d.
    (maxval, minval) = (fgradabs.max(), fgradabs.min())
    fgradabs = np.interp(fgradabs, (minval, maxval), (0, 1))
    fgradabs = cut(fgradabs, c)

    # Vis bilde
    plt.imshow(fgradabs, cmap='gist_gray')
    plt.show()


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    main()
