import os
os.system('cls')


def typed(new_type):
    def types_decorator(func):
        def wrapper(*args):
            new_args = []
            for arg in args:
                if not isinstance(arg, new_type):
                    new_args.append(new_type(arg))
                else:
                    new_args.append(arg)
            return func(*new_args)
        return wrapper
    return types_decorator


@typed(new_type=str)
def add_1(a, b):
    return a + b


print(add_1("3", 5))
print(add_1(5, 5))
print(add_1('a', 'b'))


def use_int_type(my_var):  # Для выбора new_type в аргументах декоратора: 1 -int, 0 -float
    return bool(my_var)


@typed(new_type=int if use_int_type(1) else float)  # use_int_type(1) - int, use_int_type(0) - float
def add_2(a, b, c):
    return a + b + c


print(add_2(5, 6, 7))
print(add_2('5', 6, 7))
print(add_2(0.1, 0.2, 0.4))
