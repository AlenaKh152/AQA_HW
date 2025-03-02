from typing import Union

import os
os.system('cls')

cache_dict: dict[Union[int,float], Union[int, float]] = {}


def cache(func):
    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = cache_dict.setdefault(args, func(*args))
            return result
    return wrapper


@cache
def power(a):
    return a ** a


print(power(5))
print(cache_dict)
print(power(4))
print(cache_dict)
print(power(5))
print(cache_dict)
print(power(3))
print(cache_dict)
print(power(4))
print(cache_dict)
