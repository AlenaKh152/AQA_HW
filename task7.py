test_string = input('Enter the string: ')
number = int(input())


def process_string(string, num):
    end_part = string[:num - 1]
    new_str = string[:num] + end_part[::-1]
    return  new_str

print(process_string(test_string, number))

# abcdefghijklmnopqrstuvwxyz
