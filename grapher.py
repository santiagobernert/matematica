import matplotlib.pyplot as plt
import numpy as np


def graph(function):
    x = np.arange(-11, 11, 1)
    #a, n1, o1, b, n2, o2, c, n3, o3, d, n4 = function.get()
    #array = np.fromstring(function)
    y = eval(function)
    plt.title(function)
    plt.ylim([-100, 100])
    plt.grid()
    plt.plot(x, y)
    plt.show()
