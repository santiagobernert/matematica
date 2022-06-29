
def getFunctionType(function):
    if ') / (' in function:
        function_type = 'Rational'
        functions = function.split(' / ')
        return function_type, functions
    elif '**(0' in function or '**0' in function:
        function_type = 'Irrational'
        return function_type, function
    else:
        function_type = 'Polinomical'
        return function_type, function

def getFunctionInfo(function):
    function_type = getFunctionType(function)[0]
    domain = getDomain(function_type, function)
    range = getRange(function_type, function)
    y_intercept = getYIntercept(function_type, function)
    zero = getZero(function_type, function)
    positivity = getPositivity(function_type, function)
    negativity = getNegativity(function_type, function)
    vertical_asintote = getVerticalAsintote(function_type, function)
    horizontal_asintote = getHorizontalAsintote(function_type, function)
    return domain, range, y_intercept, zero, positivity, negativity, vertical_asintote, horizontal_asintote

def getDomain(function_type, function):
    if function_type == 'Polinomical':
        return 'ℝ'
    elif function_type == 'Rational':
        pass
    elif function_type == 'Irrational':
        if '0.5' in function or '0.25' in function or '0.125' in function:
            pass
        
def getRange(function_type, function):
    return '10'

def getYIntercept(function_type, function):
    return '10'

def getZero(function_type, function):
    return '10'

def getPositivity(function_type, function):
    return '10'

def getNegativity(function_type, function):
    return '10'

def getVerticalAsintote(function_type, function):
    return '10'

def getHorizontalAsintote(function_type, function):
    return '10'