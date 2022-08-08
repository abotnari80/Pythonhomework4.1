#Вычислить число c заданной точностью d
#Пример:- при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$ 
from math import pi

def FindLength(y):
    s = str(y)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1

lengthOfPi = float(input('Введите вид числа Пи (d): '))
roundOfPi = FindLength(lengthOfPi)
print(roundOfPi)

#k = 1
#x = 0
#for k in range(1, 1000000):
#    x = x+4*((-1)**(k+1))/(2*k-1)
print(round(pi, roundOfPi))