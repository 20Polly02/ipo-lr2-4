import math
from math import fabs
x=int(input("Введите значение х"))
print("x=",x)
y=int(input("Введите значение у"))
print("y=",y)
z=int(input("Введите значение z от 0 до 1"))
print("z=",z)
m=x-y
b=(((10*(x**1/3)+(x**(y+2)))**1/2)*(((math.asin(z))**2)-fabs(m)))
print("Ответ:", b)
