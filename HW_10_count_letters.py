import os
os.system('cls')


def enter_initial_string():
    return input('Введите строку: ')


def string_processing(my_string: str) -> str:
    my_list = list(my_string)
    new_list = []
    for i in my_list:
        count = 1
        new_list.append(i)
        for j in my_list[my_list.index(i) + 1:]:
            if i == j:
                count += 1
                del my_list[my_list.index(j)]
            else:
                break
        if count > 1:
            new_list.append(str(count))
    return ('').join(new_list)


def show_result_string():
    initial_string = enter_initial_string()
    print(f'Итого: {string_processing(initial_string)}')


show_result_string()


if __name__ == '__main__':
    assert string_processing("cccbba") == "c3b2a"
    assert string_processing("abeehhhhhccced") == "abe2h5c3ed"
    assert string_processing("aaabbceedd") == "a3b2ce2d2"
    assert string_processing("abcde") == "abcde"
    assert string_processing("aaabbdefffff") == "a3b2def5"
