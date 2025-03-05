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
            print(f'Success reserve. {self.book_name} has been reserved by {reader.name}.')
        elif not self.reserve_flag:
            self.reserve_flag = True
            self.reserve_reader = reader
            print(f'Success reserve. {self.book_name} has been reserved by {reader.name}.')
        else:
            print(f'Reserve error. {self.book_name} is already reserved/received.')


    def cancel_reserve(self, reader):
        if self.reserve_flag and self.reserve_reader == reader:
            self.reserve_flag = False
            self.reserve_reader = None
            print(f'Book reservation was cancelled by {reader.name}.')
        elif self.reserve_flag and self.reserve_reader != reader:
            print(f'Reader {reader.name} has no active {self.book_name} reservation to cancel')
        else:
            print(f'No active reserve. {self.book_name} can be reserved.')


    def get_book(self, reader):
        if self.reserve_flag and self.reserve_reader == reader and not self.current_reader:
            self.reserve_flag = False
            self.reserve_reader = None
            self.current_reader = reader
            print(f'Success receive. {self.book_name} was successfully received by {reader.name}!')
        elif self.reserve_flag and self.reserve_reader == reader and self.current_reader != reader:
            print(f'Receive error. {self.book_name} is still used by another reader!')
        else:
            print(f'Receive error. {reader.name} has no reservation for {self.book_name}.')


    def return_book(self, reader):
        if self.current_reader == reader:
            self.current_reader = None
            print(f'Success return. {self.book_name} was returned by {reader.name}.')
        else:
            print(f'Return error. {self.book_name} was not received by {reader.name}.')


class Reader:

    def __init__(self, name):
        self.name = name


    def reserve_book(self, book):
        book.reserve(self)


    def cancel_reserve(self, book):
        book.cancel_reserve(self)


    def get_book(self, book):
        book.get_book(self)


    def return_book(self, book):
        book.return_book(self)


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
