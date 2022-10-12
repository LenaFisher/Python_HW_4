# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.   $10^{-1} ≤ d ≤10^{-10}$

from math import *
accuracy =float(input("введите заданную точность: "))
count=0
while accuracy<1:
    accuracy=accuracy*10
    count=count+1
digit_pi=str(pi)
print(digit_pi[:(count+2)])




