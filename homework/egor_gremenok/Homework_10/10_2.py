def finish_me(func):
    def wrapper(txt, reps):
        for _ in range(reps):
            func(txt)
    return wrapper


@finish_me
def example(text):
    print(text)


repeats = int(input())
example("print me", repeats)
