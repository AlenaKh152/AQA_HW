from dateutil.parser import parse
import os
os.system('cls')

date1 = parse(input('Enter the first date (YYYY-MM-DD): '))
date2 = parse(input('Enter the second date (YYYY-MM-DD): '))


def days_difference(date_1, date_2):
    delta = abs((date_1 - date_2).days)
    print(f'Number of days between dates: {delta}.')


days_difference(date1, date2)
