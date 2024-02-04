# Higher order Function = a. function that either :
#                         1. accepts a function as an argument
#                         or
#                         2. returns a function
#                         (functions are also treated as objects)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x

    return dividend


divide = divisor(10)
print(divide(100))
