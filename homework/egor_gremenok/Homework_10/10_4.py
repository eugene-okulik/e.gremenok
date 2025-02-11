PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list = " ".join(PRICE_LIST.split('\n')).split(' ')  # можно через replace, но так веселее

items = [price_list[x] for x in range(len(price_list)) if x % 2 == 0]  # list comprehension
price_int = [int(price_list[x][:-1]) for x in range(len(price_list)) if x % 2 != 0]

# items = list(filter(lambda x: price_list.index(x) % 2 == 0, price_list))  # вариант вообще без циклов
# price = list(filter(lambda x: price_list.index(x) % 2 != 0, price_list))
# price_int = list(map(lambda x: int(x[:-1]), price))

price_dict = dict(zip(items, price_int))

print(price_dict)
