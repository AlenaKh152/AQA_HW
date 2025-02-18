import os
os.system('cls')

n = int(input('Введите число строк пирамиды'))

for i in range(n):
    s = (2 * i + 1) * '*'
    print(s.center(2 * n + 1))
