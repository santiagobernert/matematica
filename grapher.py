import matplotlib.pyplot as plt
import numpy as np
from info import getFunctionType

def graph(function, pointInX=0):
    #GETTING FUNCTION TYPE
    function_type = getFunctionType(function)
    #DEFINING X AXIS RANGE
    x = np.arange(-11, 11, 1)
    #EVALUATING THE FUNCTION
    y = eval(function)
    pointInY = evalInPoint(str(pointInX), function)
    #DEFINING THE GRAPH'S TITLE
    plt.title(f'{function_type}: {function}')
    #DEFINING Y AXIS RANGE
    plt.ylim([-100, 100])
    #SHOW AXES
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    #SHOW LINES IN THE GRAPH
    plt.grid()
    plt.plot(np.where(x == pointInX-11), [pointInY], marker='.', markersize=10, markeredgecolor="red", markerfacecolor="red")
    plt.plot(x, y)
    plt.show()

def evalInPoint(pointInX, function):
    f_type = getFunctionType(function)
    if f_type == 'Irrational' and int(pointInX) < 0:
        pointInY = 'Imaginary number'
    else:
        pointInY = eval(function.replace('x', pointInX))
    print(pointInX, pointInY)
    return pointInY
