import os
os.system('cls')


def enter_initial_string():
    return input('Введите строку: ')


def delete_symbol(cur_string: str):
    str_list = list(cur_string)
    while "#" in str_list and len(str_list) > 1:
        del str_list[str_list.index('#') - 1]
        del str_list[str_list.index('#')]
    else:
        if "#" in str_list and len(str_list) == 1:
            del str_list[0]
    return ('').join(str_list)


def show_final_string():
    my_string = enter_initial_string()
    final_string = delete_symbol(my_string)
    if final_string:
        print(f'Обработанная строка: {final_string}')
    else:
        print('Обработанная строка не содержит символов')


show_final_string()


# assert solution("a#bc#d") == "bd"
# assert solution("abc#d##c") == "ac"
# assert solution("abc##d######") == ""
# assert solution("#######") == ""
# assert solution("") == ""
