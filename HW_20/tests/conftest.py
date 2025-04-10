import pytest

import logging
from logging import DEBUG, basicConfig, FileHandler

from HW_20.source.HW_12_bank_deposit_copy import Bank
from HW_20.source.HW_12_library_copy import Book, Reader


def pytest_addoption(parser):
    parser.addoption("--loglevel", action="store", default="ERROR")


@pytest.fixture(scope='session', autouse=True)
def test_option(request):
    log_lev = request.config.getoption("loglevel")
    logger = logging.getLogger("Test_logger")
    FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    file_handler = FileHandler('test_20_actions.log')
    file_handler.setLevel(log_lev)
    basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler])
    logger.addHandler(file_handler)
    logger.setLevel(log_lev)


@pytest.fixture
def create_bank():
    bank = Bank()
    return bank


@pytest.fixture
def create_book1():
    book1 = Book("First book", "Tom", 400, "0006754023")
    return book1


@pytest.fixture
def create_book2():
    book2 = Book("Second book", "Jerry", 500, "00022222")
    return book2


@pytest.fixture
def create_reader1():
    reader1 = Reader('Vasya')
    return reader1


@pytest.fixture
def create_reader2():
    reader2 = Reader('Petya')
    return reader2


def pytest_html_report_title(report):
    report.title = "Test HW20 report"
