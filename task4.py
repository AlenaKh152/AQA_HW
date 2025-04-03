def add_one():
    num_list = list(input('Enter the number: '))
    new_num_list =  list(str(int(''.join(num_list)) + 1))
    print(new_num_list)


add_one()
