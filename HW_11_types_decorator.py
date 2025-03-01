import os
os.system('cls')


def typed(new_type):
    def types_decorator(func):
        def wrapper(*args):
            new_args = []
            for arg in args:
                if type(arg) != new_type:
                    new_args.append(new_type(arg))
                else:
                    new_args.append(arg)
            return func(*new_args)
        return wrapper
    return types_decorator


@typed(new_type=str)
def add(a, b):
    return a + b


print(add("3", 5))
print(add(5, 5))
print(add('a', 'b'))


@typed(new_type=int)
def add(a, b, c):
    return a + b + c


print(add(5, 6, 7))
print(add('5', 6, 7))


@typed(new_type=float)
def add(a, b, c):
    return a + b + c


print(add(0.1, 0.2, 0.4))
