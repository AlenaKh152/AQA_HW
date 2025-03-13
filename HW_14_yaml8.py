import yaml

# to_yaml = {'Book1': ['Author1', '1991'],'Book2': ['Author2', '1992'],'Book3': ['Author3', '1993']}

# with open('C:/Users/Admin/Documents/AQA_HW/data_yaml.yaml', 'w') as file:
# yaml.dump(to_yaml, file)


def add_book(name, author, year):
    with open('C:/Users/Admin/Documents/AQA_HW/data_yaml.yaml', 'r') as file:
        start_data = yaml.safe_load(file)
    key = name
    value = [author, year]
    if key not in start_data.keys():
        start_data[key] = value
        with open('C:/Users/Admin/Documents/AQA_HW/data_yaml.yaml', 'w') as file:
            yaml.dump(start_data, file)
        print(f'Book {key} was added.')
    else:
        print(f'Book {key} is already exist.')


add_book('Book4', 'Author4', 1994)
