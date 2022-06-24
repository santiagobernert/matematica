import matplotlib.pyplot as plt
import numpy as np

def getFunctionType():
    pass

def graph(function):
    #DEFINING X AXIS RANGE
    x = np.arange(-11, 11, 1)
    #EVALUATING THE FUNCTION
    y = eval(function)
    #DEFINING THE GRAPH'S TITLE
    plt.title(function)
    #DEFINING Y AXIS RANGE
    plt.ylim([-100, 100])
    #SHOW LINES IN THE GRAPH
    plt.grid()
    plt.plot(x, y)
    plt.show()
