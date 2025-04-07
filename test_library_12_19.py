import unittest
from HW_12_library import Book, Reader


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("First book", "Tom", 400, "0006754023")
        self.book2 = Book("Second book", "Jerry", 500, "00022222")
        self.reader1 = Reader('Vasya')
        self.reader2 = Reader('Petya')

    # Тест позитивный: резерв книги, которая не зарезервирована и не на руках
    def test_positive1_reserve(self):
        self.reader1.reserve_book(self.book1)
        self.assertTrue(self.book1.reserve_flag)
        self.assertEqual(self.book1.reserve_reader, self.reader1)

    # Тест позитивный: резерв книги, которая не зарезервирована, но находится на руках
    def test_positive2_reserve(self):
        self.reader1.reserve_book(self.book1)
        self.reader1.get_book(self.book1)
        self.reader2.reserve_book(self.book1)
        self.assertTrue(self.book1.reserve_flag)
        self.assertEqual(self.book1.reserve_reader, self.reader2)

    # Тест позитивный: резерв нескольких книг одним пользователем
    def test_positive3_reserve(self):
        self.reader1.reserve_book(self.book1)
        self.reader1.reserve_book(self.book2)
        self.assertTrue(self.book1.reserve_flag)
        self.assertTrue(self.book2.reserve_flag)
        self.assertEqual(self.book1.reserve_reader, self.reader1)
        self.assertEqual(self.book2.reserve_reader, self.reader1)

    # Тест негативный: резерв книги, которая уже зарезервирована
    def test_negative_reserve(self):
        self.reader1.reserve_book(self.book1)
        self.reader2.reserve_book(self.book1)
        self.assertNotEqual(self.book1.reserve_reader, self.reader2)

    # Тест позитивный: отмена резерва пользователем, который сделал резерв книги
    def test_positive_cancel_reserve(self):
        self.reader1.reserve_book(self.book1)
        self.reader1.cancel_reserve(self.book1)
        self.assertFalse(self.book1.reserve_flag)
        self.assertIsNone(self.book1.reserve_reader)

    # Тест негативный: отмена резерва книги, когда резерв сделал другой пользователь
    def test_negative1_cancel_reserve(self):
        self.reader1.reserve_book(self.book1)
        self.reader2.cancel_reserve(self.book1)
        self.assertTrue(self.book1.reserve_flag)
        self.assertEqual(self.book1.reserve_reader, self.reader1)

    # Тест негативный: отмена резерва книги, когда для книги нет активного резерва
    def test_negative2_cancel_reserve(self):
        self.reader1.cancel_reserve(self.book1)
        self.assertFalse(self.book1.reserve_flag)
        self.assertIsNone(self.book1.reserve_reader)

    # Тест позитивный: получение зарезервированной книги
    def test_positive_get_book(self):
        self.reader1.reserve_book(self.book1)
        self.reader1.get_book(self.book1)
        self.assertFalse(self.book1.reserve_flag)
        self.assertIsNone(self.book1.reserve_reader)
        self.assertEqual(self.book1.current_reader, self.reader1)

    # Тест негативный: получение зарезервированной книги, когда книга ещё у другого пользователя
    def test_negative1_get_book(self):
        self.reader1.reserve_book(self.book1)
        self.reader1.get_book(self.book1)
        self.reader2.reserve_book(self.book1)
        self.reader2.get_book(self.book1)
        self.assertTrue(self.book1.reserve_flag)
        self.assertEqual(self.book1.reserve_reader, self.reader2)
        self.assertEqual(self.book1.current_reader, self.reader1)

    # Тест негативный: получение книги, зарезервированной другим пользователем
    def test_negative2_get_book(self):
        self.reader1.reserve_book(self.book1)
        self.reader2.get_book(self.book1)
        self.assertTrue(self.book1.reserve_flag)
        self.assertEqual(self.book1.reserve_reader, self.reader1)

    # Тест позитивный: возврат полученной книги
    def test_positive_return_book(self):
        self.reader1.reserve_book(self.book1)
        self.reader1.get_book(self.book1)
        self.reader1.return_book(self.book1)
        self.assertIsNone(self.book1.current_reader)

    # Тест негативный: возврат книги, полученной другим пользователем
    def test_negative1_return_book(self):
        self.reader1.reserve_book(self.book1)
        self.reader1.get_book(self.book1)
        self.reader2.return_book(self.book1)
        self.assertIsNotNone(self.book1.current_reader)
        self.assertEqual(self.book1.current_reader, self.reader1)

    # Тест негативный: возврат книги, предварительно не полученной пользователем
    def test_negative2_return_book(self):
        self.reader1.reserve_book(self.book1)
        self.reader1.return_book(self.book1)
        self.assertIsNone(self.book1.current_reader)


if __name__ == '__main__':
    unittest.main()
