'''from dateutil.parser import parse
import os
os.system('cls')

date1 = parse(input('Enter the first date: '))
date2 = parse(input('Enter the second date: '))


def days_difference(date_1, date_2):
    delta = abs((date_1 - date_2).days)
    print(f'Number of days between dates: {delta}.')


days_difference(date1, date2)'''

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import os
import os
os.system('cls')

date1 = parse(input('Enter the first date (YYYY-MM-DD): '))
date2 = parse(input('Enter the second date (YYYY-MM-DD): '))


def days_difference(date_1, date_2):
    # Вычисляем разницу между датами
    delta = relativedelta(date_1, date_2)

    # Вычисляем общее количество дней
    total_days = abs((date_1 - date_2).days)

    # Выводим результат
    print(f'Number of days between dates: {total_days}.')
    print(f'Difference is {delta.years} years, {delta.months} months, and {delta.days} days.')


days_difference(date1, date2)