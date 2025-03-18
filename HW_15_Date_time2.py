from datetime import date
from dateutil.parser import parse
import os
os.system('cls')

date1 = parse(input('Enter the date: ')).date()


def is_future_past_date(date_1):
    current_date = date.today()
    delta = (current_date - date_1).days
    if delta < 0:
        print(f'{date_1} is the FUTURE date relative to the current one.')
    elif delta > 0:
        print(f'{date_1} is the PAST date relative to the current one.')
    else:
        print(f'{date_1} is actually the current date.')


is_future_past_date(date1)
