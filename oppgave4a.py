import numpy as np
from matplotlib import pyplot as plt


def g_smoothing(nabla_f, lamdavalue):
    return 1/(np.sqrt(1+(np.square(nabla_f)/lamdavalue**2)))

# Show masterpiece
xVals = np.linspace(0, 5, 100)
lambdas = np.array([0.1, 0.5, 1, 3])

for l in lambdas:
    yVals = g_smoothing(xVals, l)
    plt.plot(xVals, yVals)
    plt.title(f"lambda value {l}")
    plt.show()





