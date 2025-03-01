import os
os.system('cls')

cache_dict = {}


def cache(func):
    def wrapper(*args):
        key = args
        if key in cache_dict:
            return cache_dict[key]
        else:
            result = cache_dict.setdefault(key, func(*args))
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
