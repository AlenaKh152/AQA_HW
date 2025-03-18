def input_data():
    try:
        n = int(input("Enter the number: "))
        return n
    except ValueError as e:
       return None


def find_sum_number(num):
    if num:
        result_sum = 0
        for i in range(1, num + 1):
            result_sum += i
        return result_sum
    else:
        return 'Error data'


n = input_data()
print(find_sum_number(n))
