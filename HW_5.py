#Заменить символ “#” на символ “/”
#в строке 'www.my_site.com#about'
string_1 = 'www.my_site.com#about'
print(string_1.replace('#', '/'))

#Напишите программу, которая добавляет
#'ing’ к словам
test_word = 'word'
print(f'{test_word}ing')

#В строке “Ivanou Ivan” поменяйте местами
#слова => "Ivan Ivanou"
string_2 = 'Ivanou Ivan'
list_2 = string_2.split()
result_string_2 = (' ').join(list_2[::-1])
print(result_string_2)

#Напишите программу, которая удаляет
#пробел в начале, в конце строки
string_3 = ' Test string 3 '
result_string_3 = string_3.strip()
print(result_string_3)

#Исправьте данное имя собственное так,
#чтобы оно соответствовало
#этому утверждению. "pARiS" >> "Paris"
test_name = 'pARis'
print(test_name.title())

#Перевести строку в список
#"Robin Singh" => ["Robin”, “Singh"]
string_4 = 'Robin Singh'
list_4 = string_4.split()
print(list_4)

#"I love arrays they are my favorite" =>
#["I", "love", "arrays", "they", "are", "my", "favorite"]
string_5 = 'I love arrays they are my favorite'
list_5 = string_5.split()
print(list_5)

#Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
#Напечатайте текст: “Привет, Ivan Ivanou!
#Добро пожаловать в Minsk Belarus”
name = ['Ivan', 'Ivanou']
city, country = 'Minsk', 'Belarus'
print(f'Привет, {name[0]} {name[1]}! Добро пожаловать в {city} {country}')

#Дан список
#["I", "love", "arrays", "they", "are", "my", "favorite"]
#сделайте из него строку =>
#"I love arrays they are my favorite"
list_6 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
string_6 = (' ').join(list_6)
print(string_6)

#Создайте список из 10 элементов,
#вставьте на 3-ю позицию новое значение,
#удалите элемент из списка под индексом 6
list_7 = list(range(1, 11))
list_7.insert(2, 'New value')
del list_7[6]
print(list_7)