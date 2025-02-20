import os
os.system('cls')


def init():
    return input('Введите номер карты: ')


def check(number):
    return bool(number.isdigit())


def validate_card():
    number = init()
    if not check(number):
        return 'Ошибка ввода: Номер карты может содержать только цифры.'
    else:
        num = number[::-1]
        list_odd = [int(num[i]) for i in range(0, len(num), 2)]
        list_even = [int(num[i]) * 2 if int(num[i]) * 2 < 9
                     else int(num[i]) * 2 - 9 for i in range(1, len(num), 2)]
        final_num = sum(list_odd) + sum(list_even)
        return bool(final_num % 10 == 0)


print(validate_card())

# print(validate_card('4561261212345464'))  # == False
# print(validate_card('4561261212345467'))  # == True
# print(validate_card('378282246310005'))   # == True
