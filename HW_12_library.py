import os
os.system('cls')


class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserve_flag = False
        self.reserve_reader = None
        self.current_reader = None

    def reserve(self, reader):
        if not self.reserve_flag and self.current_reader != reader:
            self.reserve_flag = True
            self.reserve_reader = reader
            return True
        elif not self.reserve_flag:
            self.reserve_flag = True
            self.reserve_reader = reader
            return True
        else:
            return False

    def cancel_reserve(self, reader):
        if self.reserve_flag and self.reserve_reader == reader:
            self.reserve_flag = False
            self.reserve_reader = None
            return True
        else:
            return False

    def get_book(self, reader):
        if self.reserve_flag and self.reserve_reader == reader and not self.current_reader:
            self.reserve_flag = False
            self.reserve_reader = None
            self.current_reader = reader
            return True
        else:
            return False

    def return_book(self, reader):
        if self.current_reader == reader:
            self.current_reader = None
            return True
        else:
            return False


class Reader:

    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        if book.reserve(self):
            print(f'Success reserve. {book.book_name} has been reserved by {self.name}.')
        else:
            print(f'Reserve error. {book.book_name} is already reserved/received.')

    def cancel_reserve(self, book):
        if book.cancel_reserve(self):
            print(f'Success cancel. Book reservation was cancelled by {self.name}.')
        else:
            print(f'Cancel error. No active reservation for {book.book_name}.')

    def get_book(self, book):
        if book.get_book(self):
            print(f'Success receive. {book.book_name} was successfully received by {self.name}!')
        else:
            print(f'Receive error. {book.book_name} is not reserved or is still used!')

    def return_book(self, book):
        if book.return_book(self):
            print(f'Success return. {book.book_name} was returned by {self.name}.')
        else:
            print(f'Return error. {book.book_name} was not received by {self.name}.')


book1 = Book(book_name="First book", author="Tom", num_pages=400, isbn="0006754023")
book2 = Book(book_name="Second book", author="Jerry", num_pages=500, isbn="00022222")

vasya = Reader('Vasya')
petya = Reader('Petya')

# vasya.reserve_book(book1)
# petya.reserve_book(book1)
# vasya.return_book(book1)
# vasya.get_book(book1)
# petya.reserve_book(book1)
# petya.get_book(book1)
# vasya.reserve_book(book1)
# vasya.return_book(book1)
# petya.reserve_book(book1)
# petya.get_book(book1)
# vasya.reserve_book(book1)
# petya.return_book(book1)
# petya.cancel_reserve(book1)
# vasya.return_book(book1)
# vasya.cancel_reserve(book1)
# petya.reserve_book(book1)
