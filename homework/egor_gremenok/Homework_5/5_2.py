res_1 = 'результат операции: 42'
res_2 = 'результат операции: 514'
res_3 = 'результат работы программы: 9'

num_1 = int(res_1[res_1.index(':') + 2:])
num_2 = int(res_2[res_2.index(':') + 2:])
num_3 = int(res_3[res_3.index(':') + 2:])

print(f'{num_1 + 10}')
print(f'{num_2 + 10}')
print(f'{num_3 + 10}')
