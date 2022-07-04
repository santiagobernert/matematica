
def getFunctionType(function):
    if ') / (' in function:
        function_type = 'Rational'
        return function_type
    elif '**(0' in function or '**0' in function:
        function_type = 'Irrational'
        return function_type
    else:
        function_type = 'Polinomical'
        return function_type
