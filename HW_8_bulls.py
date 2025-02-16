import os
os.system('cls')

n = '6521'
n_tup = tuple(str(n))

def init():                                                  # ввод числа пользователем
    num = input('Введите четырехзначное число ')
    return num


def is_num_valid(num):                                       # проверка на повторяющиеся цифры и длину введенного числа
    is_valid = ''
    if len(num) != 4:
        is_valid = 'length'
    else:
        for i in num:
            if num.count(i) == 1:
                is_valid = 'true'
            elif num.count(i) > 1:
                is_valid = 'false'
                break
    return is_valid


def count_choice(n_tup, num):                                # подсчет быков и коров
    num_tup = tuple(num)
    bulls = 0
    cows = 0
    for i in num_tup:
        if i in n_tup and num_tup.index(i) == n_tup.index(i):
            bulls += 1
        elif i in n_tup:
            cows += 1
    if bulls == 4:
        print('Вы выиграли!')
        repeat = 0
    else:
        print(f'{cows} коровы, {bulls} быков')
        repeat = 1
    return repeat


def main():
    while True:
        num = init()
        check = is_num_valid(num)
        if check == 'length':
            print("Введенное число не является четырехзначным!")
        elif check == 'false':
            print("Число содержит повторяющиеся цифры, попробуйте ещё раз!")
        else:
            is_repeat = count_choice(n_tup, num)
            if is_repeat == 1:
                continue
            else:
                break


main()
