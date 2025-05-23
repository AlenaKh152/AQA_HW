import logging

logger = logging.getLogger("Test_logger")


class ReserveError(Exception):
    pass


class CancelError(Exception):
    pass


class ReceiveError(Exception):
    pass


class ReturnError(Exception):
    pass


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
            logger.info('Success1 reserve.')
            return True
        elif not self.reserve_flag:
            self.reserve_flag = True
            self.reserve_reader = reader
            logger.info('Success2 reserve.')
            return True
        else:
            logger.info('Error1 reserve.')
            return False

    def cancel_reserve(self, reader):
        if self.reserve_flag and self.reserve_reader == reader:
            self.reserve_flag = False
            self.reserve_reader = None
            logger.info('Success1 cancel.')
            return True
        else:
            logger.info('Error1 cancel.')
            return False

    def get_book(self, reader):
        if self.reserve_flag and self.reserve_reader == reader and self.current_reader is None:
            self.reserve_flag = False
            self.reserve_reader = None
            self.current_reader = reader
            logger.info('Success1 get.')
            return True
        else:
            logger.info('Error1 get.')
            return False

    def return_book(self, reader):
        if self.current_reader == reader:
            self.current_reader = None
            logger.info('Success1 return.')
            return True
        else:
            logger.info('Error1 return.')
            return False


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        if book.reserve(self):
            print(f'Success reserve. {book.book_name} has been reserved by {self.name}.')
            return f'Success reserve. {book.book_name} has been reserved by {self.name}.'
        else:
            print(f'Reserve error. {book.book_name} is already reserved/received.')
            raise ReserveError(f'Reserve error. {book.book_name} is already reserved/received.')

    def cancel_reserve(self, book):
        if book.cancel_reserve(self):
            print(f'Success cancel. Book reservation was cancelled by {self.name}.')
            return f'Success cancel. Book reservation was cancelled by {self.name}.'
        else:
            print(f'Cancel error. No active reservation for {book.book_name}.')
            raise CancelError(f'Cancel error. No active reservation for {book.book_name}.')

    def get_book(self, book):
        if book.get_book(self):
            print(f'Success receive. {book.book_name} was successfully received by {self.name}!')
            return f'Success receive. {book.book_name} was successfully received by {self.name}!'
        else:
            print(f'Receive error. {book.book_name} is not reserved or is still used!')
            raise ReceiveError(f'Receive error. {book.book_name} is not reserved or is still used!')

    def return_book(self, book):
        if book.return_book(self):
            print(f'Success return. {book.book_name} was returned by {self.name}.')
            return f'Success return. {book.book_name} was returned by {self.name}.'
        else:
            print(f'Return error. {book.book_name} was not received by {self.name}.')
            raise ReturnError(f'Return error. {book.book_name} was not received by {self.name}.')
