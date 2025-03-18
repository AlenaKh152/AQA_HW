import os
os.system('cls')

from logging import getLogger, ERROR, DEBUG, basicConfig, StreamHandler, FileHandler

logger = getLogger()
FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

file_handler = FileHandler('generator1_actions.log')
file_handler.setLevel(DEBUG)
console_handler = StreamHandler()
console_handler.setLevel(ERROR)

basicConfig(level=DEBUG, format=FORMAT, handlers=[console_handler, file_handler])


def init_number():
    try:
        number = int(input('Enter the integer number: '))
        if number > 0 and isinstance(number, int):
            logger.debug('Initial number is %s', number)
            return number
        else:
            logger.debug('Input is not a positive integer number: %s', number)
            return None
    except ValueError:
        logger.debug('Input is not integer')
        return None


def my_gen_func():
    n = init_number()
    if n:
        num = 1
        while num <= n:
            yield num
            num += 1


def sum_init():
    result = 0
    numbers = list(my_gen_func())
    for num in numbers:
        result += num
    if result > 0:
        logger.info('Sum of integers is: %s', result)
        print(f'Sum of integers is: {result}')
    else:
        print('Input is not integer or positive integer.')


sum_init()
