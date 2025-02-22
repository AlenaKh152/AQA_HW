import os
os.system('cls')


def find_front_number(n, first_number):
    if first_number < n / 2:
        front_number = n / 2 + first_number
    else:
        front_number = (n / 2 + first_number) - n
    print(int(front_number))


find_front_number(10, 6)
find_front_number(10, 2)
find_front_number(10, 4)
find_front_number(12, 6)
