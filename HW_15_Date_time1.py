import os
from dateutil.parser import parse

os.system('cls')

date1 = parse(input('Enter the first date (YYYY-MM-DD): '))
date2 = parse(input('Enter the second date (YYYY-MM-DD): '))


def days_difference(date_1, date_2):
    diff = abs((date_1 - date_2).days)
    return diff


print(f'Number of days between dates: {days_difference(date1, date2)}')
