
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


def blur(img, iterations, strength):
    blurred = copyImg(img)

    for i in range(iterations):
        fx = f_discrete_x(blurred)
        fy = f_discrete_y(blurred)
        fxx = f_discrete_x(fx)
        fyy = f_discrete_y(fy)

        blurred += strength * (fxx + fyy)
        print("blur iteration", i + 1)

    return blurred


# To prevent under and overflow problems
def copyImg(img):
    return img.copy().astype("float64")


def g_smoothing(nabla_f, lamdavalue):
    return 1/(np.sqrt(1+(np.square(nabla_f)/lamdavalue**2)))


def main(blur_iterations, blur_strength, cut_treshold, lambdavalue):
    # loads the image into array with one channel
    img = np.asarray(Image
                     .open('data/image001.png', mode='r')
                     .convert('L'))

    # Blur image before edge-detection
    blurred = blur(img,
                   blur_iterations,
                   blur_strength)

    # Partial diff per direction
    fx = f_discrete_x(blurred)
    fy = f_discrete_y(blurred)

    # Calculating gradient length
    length = f_gradlen(fx, fy)

    # Oppgave 1 d.
    # Alter number range

    # Run smoothing algorithm
    smoothie = g_smoothing(length, lambdavalue)

    interpd = np.interp(length,
                        (length.min(), length.max()),
                        (0, 1))
    i_like_your_cut_g = cut(smoothie, cut_treshold)


    # Show masterpiece
    plt.imshow(i_like_your_cut_g, cmap='binary')
    plt.show()


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image

    main(cut_treshold=0.25,
         blur_iterations=10,
         blur_strength=0.2,
         lambdavalue=2)
