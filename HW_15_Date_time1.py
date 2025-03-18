import os
os.system('cls')

from datetime import datetime
from dateutil.parser import parse

date1 = parse(input('Enter the first date: '))
date2 = parse(input('Enter the first date: '))

def days_difference(date_1, date_2):
    delta = abs((date_1 - date_2).days)
    print(f'Number of days between dates: {delta}.')

days_difference(date1, date2)
