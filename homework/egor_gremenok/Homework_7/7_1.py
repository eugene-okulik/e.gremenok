from random import randint

secret = randint(0, 9)

while True:
    answer = int(input("Попробуйте угадать цифру: "))
    if answer != secret:
        print("Попробуйте снова")
        continue
    else:
        print("Поздравляю! Вы угадали!")
        break
