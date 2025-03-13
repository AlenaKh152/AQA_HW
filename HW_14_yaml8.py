import yaml


def read_books():
    with open('data_yaml.yaml', 'r',  encoding="utf-8") as file:
        start_data = yaml.safe_load(file)
    return start_data


def add_book(name, author, year):
    current_data = read_books()
    key = name
    value = [author, year]
    if key not in current_data.keys():
        current_data[key] = value
        with open('data_yaml.yaml', 'w',  encoding="utf-8") as file:
            yaml.dump(current_data, file)
        print(f'Book {key} was added.')
    else:
        print(f'Book {key} is already exist.')


add_book('Book5', 'Author5', 1995)
