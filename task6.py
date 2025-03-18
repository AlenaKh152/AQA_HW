def file_process(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        text = file.readlines()

    lines_count = len(text)

    words_list = (''.join(text)).split()
    words_count = len(words_list)
    letters_list = ''.join(words_list)
    letters_count = len(letters_list)

    new_lines = f"Lines count: {lines_count}\nWords count: {words_count}\nLetters count: {letters_count}\n"

    with open('file_task6.txt', 'a', encoding="utf-8") as file:
        file.write(new_lines)

    print(new_lines)

file_process('file_task6.txt')
