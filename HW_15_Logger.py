from logging import getLogger, basicConfig, DEBUG, ERROR, StreamHandler
from logging.handlers import  TimedRotatingFileHandler
import os
os.system('cls')

logger = getLogger()
FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

file_handler = TimedRotatingFileHandler("user_actions.log", when='d', interval=1, backupCount=7)
file_handler.setLevel(DEBUG)

console_handler = StreamHandler()
console_handler.setLevel(ERROR)

basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, console_handler])


def enter_data():
    data_list = input("Enter data to evaluate: ").split()
    logger.info('Data list:  %s', data_list)
    return data_list


def count_average():
    try:
        data_list = enter_data()
        num_list = [int(data_list[i]) for i in range(len(data_list))]
        logger.debug('Num_list from Data_list:  %s', num_list)
        count_avg = round(sum(num_list) / len(num_list), 2)
        logger.info('Average is %s', count_avg)
        return count_avg
    except Exception as e:
        logger.error('Exception: %s', e)
        return None


def main():
    result = count_average()
    if not result:
        logger.error('Invalid data entered.')
    else:
        print(f'Average is {result}')


main()
