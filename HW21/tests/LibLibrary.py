from HW21.source.HW_12_library_21 import (Book, Reader, ReserveError,
                                          CancelError, ReceiveError, ReturnError)


class LibLibrary:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_reader(self, name):
        reader = Reader(name)
        self.readers.append(reader)
        return reader

    def add_book(self, book_name, author, num_pages, isbn):
        book = Book(book_name, author, num_pages, isbn)
        self.books.append(book)
        return book

    def reserve_book(self, reader_name, book):
        reader = next((read for read in self.readers if read.name == reader_name), None)
        try:
            return reader.reserve_book(book)
        except ReserveError as e:
            return str(e)

    def cancel_reserve(self, reader_name, book):
        reader = next((read for read in self.readers if read.name == reader_name), None)
        try:
            return reader.cancel_reserve(book)
        except CancelError as e:
            return str(e)

    def get_book(self, reader_name, book):
        reader = next((read for read in self.readers if read.name == reader_name), None)
        try:
            return reader.get_book(book)
        except ReceiveError as e:
            return str(e)

    def return_book(self, reader_name, book):
        reader = next((read for read in self.readers if read.name == reader_name), None)
        try:
            return reader.return_book(book)
        except ReturnError as e:
            return str(e)
