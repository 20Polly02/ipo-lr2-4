x=input("Введите значение х")
print("x=",x)
y=input("Введите значение у")
print("y=",y)
z=input("Введите значение z от 0 до 1")
print("z=",z)
m=(int(x)-int(y))
import math
from math import fabs
b=(((10*((int(x)**1/3)+(int(x)**(int(y)+2))))**1/2)*(((math.asin(float(z)))**2)-fabs(m)))
print("Ответ:", b)