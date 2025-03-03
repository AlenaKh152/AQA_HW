import os
os.system('cls')


def is_function_result_num(func):
    def wrapper(*args):
        result = func(*args)
        if not isinstance(result, (float, int)):
            return False
        else:
            return True
    return wrapper


@is_function_result_num
def first_function_to_be_checked(a, b):
    return a + b


print(first_function_to_be_checked(5, 8))
print(first_function_to_be_checked(1.95, 2.89))
print(first_function_to_be_checked('Hello', 'Spring'))
print(first_function_to_be_checked([1, 2, 3], ['a', 'b', 'c']))
