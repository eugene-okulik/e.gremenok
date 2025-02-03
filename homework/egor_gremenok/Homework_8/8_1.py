from random import randint


def get_bonus(money, luck):
    if luck == True:  # можно опустить True, но так красивше
        bonus = randint(100, 1000)
        print(f'Бонус: {bonus}')  # для проверки бонуса
    else:
        bonus = 0
    money += bonus
    return money


while True:
    salary = int(input('Зарплата: '))
    choice = bool(randint(0, 1))

    if salary <= 0:
        print('Get a job!')
        break
    else:
        print(f'{salary}, {choice}, {get_bonus(salary, choice)}')
