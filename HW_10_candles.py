import os
os.system('cls')


def initial_candles_number():
    return int(input('Введите количество свечей: '))


def make_new_number():
    return int(input('Введите количество остатков для изготовления 1 свечи: '))


def count_candles(candle_number: int, make_new: int) -> int:
    count = candle_number
    rest = candle_number
    while rest >= make_new:
        new_count = rest // make_new
        rest = new_count + rest % make_new
        count += new_count
    return count


def show_result_candles_number():
    candle_num = initial_candles_number()
    make_new_num = make_new_number()
    print(f'Можно сжечь свечей: {count_candles(candle_num, make_new_num)}')


show_result_candles_number()


if __name__ == '__main__':
    assert count_candles(5, 2) == 9
    assert count_candles(1, 2) == 1
    assert count_candles(15, 5) == 18
    assert count_candles(12, 2) == 23
    assert count_candles(6, 4) == 7
    assert count_candles(13, 5) == 16
    assert count_candles(2, 3) == 2
