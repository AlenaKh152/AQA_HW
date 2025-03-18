import os
os.system('cls')


def num_squared():
    try:
        num = float(input('Enter the number: '))
        print(f'{num} in power 2 is: {num ** 2}')
    except ValueError as e:
        print(f'Invalid data format: {e}')


num_squared()


def is_even():
    try:
        num = int(input('Enter the number: '))
        if num % 2 == 0:
            print(f'{num} -- This is even number!')
        else:
            print(f'{num} -- This is odd number!')
    except ValueError as e:
        print(f'Invalid data format: {e}')


is_even()
