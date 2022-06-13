import matplotlib.pyplot as plt
import numpy as np

def graph(function):
    array = np.fromstring(function)
    plt.ylabel('y')
    plt.plot(array)
    plt.show()

graph(6)