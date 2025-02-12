def change_oper(func):
    def wrapper(num_1, num_2):
        if num_1 < 0 or num_2 < 0:
            oper = "*"
        elif num_1 > num_2:
            oper = "-"
        elif num_1 < num_2:
            oper = "/"
        elif num_1 == num_2:
            oper = "+"
        return func(num_1, num_2, oper)
    return wrapper


@change_oper
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second


x1, x2 = float(input()), float(input())

print(calc(x1, x2))
