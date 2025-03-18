def add_one():
    num_str = input('Enter the number: ')
    new_num_str = str(int(num_str) + 1)
    num_list = [int(i) for i in new_num_str]
    print(num_list)


add_one()
