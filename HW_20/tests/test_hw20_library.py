import pytest
import logging

from HW_20.source.HW_12_library_copy import ReserveError, CancelError, ReceiveError, ReturnError


class TestLibrary:
    # Тест позитивный: резерв книги, которая не зарезервирована и не на руках
    def test_positive1_reserve(self, create_book1, create_reader1):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        assert create_book1.reserve_flag is True
        logger.info('Test1 Library info: Book1 has been reserved by Reader1')

    # Тест позитивный: резерв книги, которая не зарезервирована, но находится на руках
    def test_positive2_reserve(self, create_book1, create_reader1, create_reader2):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        create_reader1.get_book(create_book1)
        create_reader2.reserve_book(create_book1)
        assert create_book1.reserve_flag is True
        assert create_book1.reserve_reader == create_reader2
        logger.info('Test2 Library info: Book1 has been reserved by Reader2')

    # Тест позитивный: резерв нескольких книг одним пользователем
    def test_positive3_reserve(self, create_book1, create_book2, create_reader1):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        create_reader1.reserve_book(create_book2)
        assert create_book1.reserve_flag is True
        assert create_book2.reserve_flag is True
        assert create_book1.reserve_reader == create_reader1
        assert create_book2.reserve_reader == create_reader1
        logger.info('Test3 Library info: Book1 and Book2 have been reserved by Reader1')

    # Тест негативный: резерв книги, которая уже зарезервирована
    def test_negative_reserve(self, create_book1, create_reader1, create_reader2):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        with pytest.raises(ReserveError):
            create_reader2.reserve_book(create_book1)
        logger.info('Test4 Library info: Book1 have not been reserved by Reader1')

    # Тест позитивный: отмена резерва пользователем, который сделал резерв книги
    def test_positive_cancel_reserve(self, create_book1, create_reader1):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        create_reader1.cancel_reserve(create_book1)
        assert create_book1.reserve_flag is False
        assert create_book1.reserve_reader is None
        logger.info('Test5 Library info: Book1 reserve was canceled by Reader1')

    # Тест негативный: отмена резерва книги, когда резерв сделал другой пользователь
    def test_negative1_cancel_reserve(self, create_book1, create_reader1, create_reader2):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        with pytest.raises(CancelError):
            create_reader2.cancel_reserve(create_book1)
        assert create_book1.reserve_flag is True
        logger.info('Test6 Library info: Book1 reserve was not canceled by Reader2')

    # Тест негативный: отмена резерва книги, когда для книги нет активного резерва
    def test_negative2_cancel_reserve(self, create_book1, create_reader1):
        logger = logging.getLogger("Test_logger")
        with pytest.raises(CancelError):
            create_reader1.cancel_reserve(create_book1)
        logger.info('Test7 Library info: Book1 reserve was not canceled by Reader1')

    # Тест позитивный: получение зарезервированной книги
    def test_positive_get_book(self, create_book1, create_reader1):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        create_reader1.get_book(create_book1)
        assert create_book1.reserve_flag is False
        assert create_book1.reserve_reader is None
        assert create_book1.current_reader == create_reader1
        logger.info('Test8 Library info: Book1  was got by Reader1')

    # Тест негативный: получение зарезервированной книги, когда книга ещё у другого пользователя
    def test_negative1_get_book(self, create_book1, create_reader1, create_reader2):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        create_reader1.get_book(create_book1)
        create_reader2.reserve_book(create_book1)
        with pytest.raises(ReceiveError):
            create_reader2.get_book(create_book1)
        logger.info('Test9 Library info: Book1  was not got by Reader2 because is used by Reader1')

    # Тест негативный: получение книги, зарезервированной другим пользователем
    def test_negative2_get_book(self, create_book1, create_reader1, create_reader2):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        with pytest.raises(ReceiveError):
            create_reader2.get_book(create_book1)
        logger.info('Test10 Library info: Book1  was not got by Reader2, it is reserved by Reader1')

    # Тест позитивный: возврат полученной книги
    def test_positive_return_book(self, create_book1, create_reader1):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        create_reader1.get_book(create_book1)
        create_reader1.return_book(create_book1)
        assert create_book1.current_reader is None
        logger.info('Test11 Library info: Book1  was returned by Reader1')

    # Тест негативный: возврат книги, полученной другим пользователем
    def test_negative1_return_book(self, create_book1, create_reader1, create_reader2):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        create_reader1.get_book(create_book1)
        with pytest.raises(ReturnError):
            create_reader2.return_book(create_book1)
        logger.info('Test12 Library info: Book1 was not returned by Reader2, it is used by Reader1')

    # Тест негативный: возврат книги, предварительно не полученной пользователем
    def test_negative2_return_book(self, create_book1, create_reader1):
        logger = logging.getLogger("Test_logger")
        create_reader1.reserve_book(create_book1)
        with pytest.raises(ReturnError):
            create_reader1.return_book(create_book1)
        logger.info('Test12 Library info: Book1 was not returned by Reader1, it was not got.')
