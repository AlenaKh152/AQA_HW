import re


def is_psw_correct():
    string = input('Enter the password: ')
    digit = re.search(r"\d", string)
    lower_ch = re.search(r"[a-zа-я]", string)
    upper_ch = re.search(r"[A-ZА-Я]", string)
    if len(string) >= 4 and digit and lower_ch and upper_ch:
        print('The password is correct.')
    else:
        print('Incorrect password.')


is_psw_correct()
