import re


sentence = ('Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова.'
            ' Смешно, не не правда ли? Не нужно портить хор хоровод.')


def fix_sentence(string):
    pattern1 = r"(\w+)\s+\1[,\.\?!-' ']"
    match1 = re.findall(pattern1, string)
    for word in match1:
        if word in string:
            string = string.replace(word, '', 1)
    pattern2 = r"\s+"
    match2 = re.split(pattern2, string)
    return (' ').join(match2)


print(fix_sentence(sentence))
