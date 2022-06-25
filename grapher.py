import matplotlib.pyplot as plt
import numpy as np
from info import getFunctionType

def graph(f):
    rational = False
    #GETTING FUNCTION TYPE
    function_type, function = getFunctionType(f)
    #DEFINING X AXIS RANGE
    x = np.arange(-11, 11, 1)
    #EVALUATING THE FUNCTION
    #checking if it is rational (because when it's rational we have to hraph two functions)
    if function_type == 'Rational':
        rational = True
        y1 = eval(function[0])
        y2 = eval(function[1])
    else:
        y = eval(function)
    #DEFINING THE GRAPH'S TITLE
    plt.title(f'{function_type}: {f}')
    #DEFINING Y AXIS RANGE
    plt.ylim([-100, 100])
    #SHOW AXES
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    #SHOW LINES IN THE GRAPH
    plt.grid()
    if rational:
        plt.plot(x, y1)
        plt.plot(x, y2)
    else:
        plt.plot(x, y)
    plt.show()
