temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
days = []

buf = list(map(lambda temp: True if temp > 28 else False, temperatures))
heat = list(filter(lambda temp: True if temp > 28 else False, temperatures))

for i in range(len(buf)):
    if buf[i] is True:
        days.append(i + 1)

max_temp = max(heat)
min_temp = min(heat)
avg_temp = sum(heat) / len(heat)

# print(*days)
# print(*heat)
print(f'Макс. t: {max_temp} - {days[heat.index(max_temp)]} день')  # берётся первое вхождение слева
print(f'Мин.  t: {min_temp} - {days[heat.index(min_temp)]} день')  # берётся первое вхождение слева
print(f'Сред. t: {avg_temp}')
