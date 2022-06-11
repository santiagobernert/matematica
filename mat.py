import os, math
#obtener la funcion exponencial, la cual esta dada por:
#e^x = 1+x/1! + x²/2! + x³/3! + ...

ex = 0
factorial = 0
x = float (input ('Ingrese el valor de x: '))
n = int (input ('Ingrese el valor de n: '))
for i in range (1, n + 1):
    print ('proceso ' + repr (i))
    if i==1:
        ex=1
        factorial=1
    factorial=factorial*i
    ex=ex+math.pow(x,i)/factorial
    print ()
print ('Valor del exponente: ' + repr (ex))
print ('Valor del factorial: ' + repr (factorial))
os.system ('pause')

