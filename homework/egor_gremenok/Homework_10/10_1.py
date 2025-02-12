def finish_me(func):
    def wrapper(txt):
        func(txt)
        print("finished")
    return wrapper


@finish_me
def example(text):
    print(text)


example("print me")
