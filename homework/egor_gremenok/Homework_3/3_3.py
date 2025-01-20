from math import sqrt

c = int(input('c = '))
d = int(input('d = '))

avg_ar = (c + d) / 2
avg_ge = sqrt(c * d)

print(f'Ср. арифметическое: {avg_ar}')
print(f'Ср. геометрическое: {avg_ge}')
