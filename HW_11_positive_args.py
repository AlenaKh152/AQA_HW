import os
os.system('cls')


def validate_arguments(func):
    def wrapper(*args):
        for arg in func(*args):
            if not isinstance(arg, (float, int)) or arg <= 0:
                raise ValueError('Не все аргументы функции положительные числа!')
        return 'Ура! Все аргументы функции положительные числа.'
    return wrapper


@validate_arguments
def function_to_check(*args):
    return args


print(function_to_check(5, 4, 1.879, 20))

# print(function_to_check(5, 0, 1.879, 20))  # check 0
# print(function_to_check(5, 4, -1.879, 20))  # check negative
# print(function_to_check([1, 2], [3, 4]))  #  check not int or float types
# print(function_to_check('5', 4, 1.879, 20)) #  check not int or float types
