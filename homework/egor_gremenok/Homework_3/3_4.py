from math import sqrt, pow

leg_1 = float(input('Катет 1: '))
leg_2 = float(input('Катет 2: '))

square = (leg_1*leg_2) / 2
hypotenuse = sqrt(pow(leg_1, 2) + pow(leg_2, 2))

print(f'Площадь: {square}')
print(f'Гипотенуза: {hypotenuse}')
