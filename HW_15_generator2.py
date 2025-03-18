import os
os.system('cls')

from logging import getLogger, DEBUG, INFO, basicConfig, StreamHandler, FileHandler

logger = getLogger()
FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

file_handler = FileHandler('generator2_actions.log')
file_handler.setLevel(DEBUG)
console_handler = StreamHandler()
console_handler.setLevel(INFO)

basicConfig(level=DEBUG, format=FORMAT, handlers=[console_handler, file_handler])


def init_range():
    try:
        start, end = int(input('Enter the start number: ')), int(input('Enter the end number: '))
        if start > end:
            logger.error("Start number can't be greater than end number")
            return None
        logger.debug('Start is %s, end is %s', start, end)
        return start, end
    except ValueError:
        logger.debug('Input is not integer')
        return None


def is_prime(num):
    divider_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divider_count += 1
    if divider_count == 2:
        return True
    else:
        return False


def my_gen_func(start, end):
    for i in range(start, end + 1):
        if is_prime(i):
            yield i


def show_prime_numbers():
    use_range = init_range()
    if not use_range:
        print('Invalid range!')
        return

    num_start, num_end = use_range
    prime_numbers = list(my_gen_func(num_start, num_end))

    if len(prime_numbers) == 0:
        logger.info('There are NO prime digits in range.')
        print('There are NO prime digits in range.')
    elif len(prime_numbers) < 10:
        logger.info('There are LESS than 10 prime digits in range.')
        print('There are LESS than 10 prime digits in range.')
    else:
        logger.debug('First 10 prime digits are %s', prime_numbers[:10])
        print('First 10 prime digits are', *prime_numbers[:10])

    print('The end!')


show_prime_numbers()
