str_1 = 'результат операции: 42'
str_2 = 'результат операции: 54'
str_3 = 'результат работы программы: 209'
str_4 = 'результат: 2'

all_str = [str_1, str_2, str_3, str_4]

def change_num (text):
    not_num = text[text.find(':') + 2:]
    num = int(not_num) + 10  # Можно было объединить с предыдущим, но, как по мне, так проще читать код
    print(num)

for i in range(len(all_str)):
    change_num(all_str[i])
