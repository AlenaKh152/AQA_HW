import os
os.system('cls')

n = '6521'
n_tup = tuple(str(n))


def init():                                                  # ввод числа пользователем
    return input('Введите четырехзначное число ')


def is_num_valid(num):                   # проверка введенного числа на повторяющиеся цифры и длину
    if len(num) != 4 or len(set(num)) != 4:
        return False
    else:
        return True


def count_choice(num):             # подсчет быков и коров
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
        return False
    else:
        print(f'{cows} коровы, {bulls} быков')
        return True


def main():
    while True:
        num = init()
        if not is_num_valid(num):
            print("Введенное число не является четырехзначным или содержит повторяющиеся цифры!")
        else:
            if not count_choice(num):
                break
            continue


main()
