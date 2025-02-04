def fibonacci():
    first = 0
    second = 1

    while True:
        yield first
        summ = first + second
        first = second
        second = summ


count = 1  # по логике ряда (0, 1, 1, 2, 3, 5, 8, 13...), где 0 и 1 первые 2 числа

for i in fibonacci():
    if count in [5, 200, 1000, 100000]:
        print(i)
    elif count > 100000:
        break  # чтобы остановить наконец программу
    count += 1
