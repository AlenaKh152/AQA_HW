import os
os.system('cls')

# Для ввода размера статуй с клавиатуры можно:
# statues = [int(num) for num in input('Введите размер имеющихся статуй через пробел').split()]
statues = [6, 2, 3, 8]
min_value = min(statues)
max_value = max(statues)
all_values = list(range(min_value, max_value + 1))
missed_count = len(all_values) - len(statues)
print(f'Не хватает {missed_count} статуй')
