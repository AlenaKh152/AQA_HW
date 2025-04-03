def my_decorator(*args, **kwargs):
    def wrapper(func):
        def my_function(*my_args, **my_kwargs):
            decorator_args = args
            decorator_kwargs = kwargs

            func_result = func(*my_args, **my_kwargs)
            return (decorator_args, decorator_kwargs), func_result
        return my_function
    return wrapper


@my_decorator(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
def identity_1(x):
    return x


result1 = identity_1(42)
print(result1[0])
print(result1[1])


@my_decorator()
def identity_2(x):
    return x


result2 = identity_2(42)
print(result2[0])
print(result2[1])
