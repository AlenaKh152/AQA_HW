def input_data():
    try:
        number = int(input("Enter the number: "))
        return number
    except ValueError:
        return None


def find_sum_number(num):
    if num:
        return ((num * (num - 1)) // 2) + num
    else:
        return 'Error data'


n = input_data()
print(find_sum_number(n))
