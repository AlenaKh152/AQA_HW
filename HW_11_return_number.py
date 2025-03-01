import os
os.system('cls')


def is_function_result_num(func):
    def wrapper(*args):
        result = func(*args)
        if not isinstance(result, (float, int)):
            print(f'{result} -- Результат функции НЕ ЯВЛЯЕТСЯ числом!')
        else:
            print(f'{result} -- Результат функции является числом.')
    return wrapper


@is_function_result_num
def first_function_to_be_checked(a, b):
    return a + b


first_function_to_be_checked(5, 8)
first_function_to_be_checked(1.95, 2.89)
first_function_to_be_checked('Hello', 'Spring')
first_function_to_be_checked([1, 2, 3], ['a', 'b', 'c'])
