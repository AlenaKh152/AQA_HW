import os
os.system('cls')


def enter_initial_string():
    return input('Введите строку: ')


def delete_symbol(cur_string: str):
    str_list = list(cur_string)
    while "#" in str_list and len(str_list) > 1:
        del str_list[str_list.index('#') - 1]
        del str_list[str_list.index('#')]
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


if __name__ == '__main__':
    assert delete_symbol("a#bc#d") == "bd"
    assert delete_symbol("abc#d##c") == "ac"
    assert delete_symbol("abc##d######") == ""
    assert delete_symbol("#######") == ""
    assert delete_symbol("") == ""
