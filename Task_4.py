# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите коэффициент: '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))
if a != 0:
    mn1 = (str(a) + "x^" + str(k) + " + ")
else:
    mn1 = (str())
if b != 0:
    mn2 = (str(b) + "x" + " + ")
else:
    mn2 = (str())
if c != 0:
    mn3 = (str(c) + " = 0")
else:
    mn3 = (str())
print(f"{mn1}{mn2}{mn3}")




