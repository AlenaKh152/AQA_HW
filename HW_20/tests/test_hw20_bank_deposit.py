import pytest
import logging

from HW_20.source.HW_12_bank_deposit_copy import (ClientAlreadyExistsError,
                                                  ClientDoesNotExistsError,
                                                  ClientHasNoDepositError)


class TestBankDeposit:
    # Тест позитивный: регистрация клиента
    def test_positive_register_client(self, create_bank):
        logger = logging.getLogger("Test_logger")
        create_bank.register_client('0001', 'Alena')
        assert create_bank.clients['0001'] == 'Alena'
        logger.info('Test1 info: client with id 0001 created.')

    # Тест негативный: регистрация клиента
    def test_negative_register_client(self, create_bank):
        logger = logging.getLogger("Test_logger")
        create_bank.register_client('0002', 'Alena')
        with pytest.raises(ClientAlreadyExistsError):
            create_bank.register_client('0002', 'Anton')
        logger.info('Test2 info: client with id 0002 Anton was not created.')

    # Тест позитивный: открытие депозита для зарегистрированного клиента
    def test_positive_open_deposit_account(self, create_bank):
        logger = logging.getLogger("Test_logger")
        create_bank.register_client('0003', 'Alena')
        create_bank.open_deposit_accaunt('0003', 2000, 2)
        assert create_bank.deposits['0003'] == [2000, 2]
        logger.info('Test3 info: deposit for client with id 0003 was opened.')

    # Тест негативный: открытие депозита для НЕ зарегистрированного клиента
    def test_negative_open_deposit_account(self, create_bank):
        logger = logging.getLogger("Test_logger")
        with pytest.raises(ClientDoesNotExistsError):
            create_bank.open_deposit_accaunt('0004', 2000, 2)
        logger.info('Test4 info: deposit for not registered client with id 0004 was not opened.')

    # Тест позитивный: закрытие депозита для зарегистрированного клиента
    def test_positive_close_deposit(self, create_bank):
        logger = logging.getLogger("Test_logger")
        create_bank.register_client('0005', 'Alena')
        create_bank.open_deposit_accaunt('0005', 2000, 2)
        create_bank.close_deposit('0005')
        assert '0005' not in create_bank.deposits
        logger.info('Test5 info: deposit for client with id 0005 was closed.')

    # Тест негативный: закрытие не открытого депозита для зарегистрированного клиента
    def test_negative1_close_deposit(self, create_bank):
        logger = logging.getLogger("Test_logger")
        create_bank.register_client('0006', 'Alena')
        with pytest.raises(ClientHasNoDepositError):
            create_bank.close_deposit('0006')
        logger.info('Test6 info: not opened deposit for client with id 0006 was not closed.')

    # Тест негативный: закрытие не открытого депозита для НЕ зарегистрированного клиента
    def test_negative2_close_deposit(self, create_bank):
        logger = logging.getLogger("Test_logger")
        with pytest.raises(ClientHasNoDepositError):
            create_bank.close_deposit('0007')
        logger.info('Test7 info: not opened deposit not registered client id 0007 was not closed.')

    # Тест позитивный: профит депозита для зарегистрированного клиента с открытым вкладом
    def test_positive_calc_deposit_interest_rate(self, create_bank):
        logger = logging.getLogger("Test_logger")
        create_bank.register_client('0008', 'Alena')
        create_bank.open_deposit_accaunt('0008', 1000, 1)
        assert create_bank.calc_deposit_interest_rate('0008') == 1104.71
        logger.info('Test8 info: deposit profit for client with id 0008 is correct.')

    # Тест негативный: профит депозита для зарегистрированного клиента БЕЗ открытого вклада
    def test_negative1_calc_deposit_interest_rate(self, create_bank):
        logger = logging.getLogger("Test_logger")
        create_bank.register_client('0009', 'Alena')
        with pytest.raises(ClientHasNoDepositError):
            create_bank.calc_deposit_interest_rate('0009')
        logger.info('Test9 info: deposit profit for client with id 0009 does not exist.')

    # Тест негативный: профит депозита для НЕ зарегистрированного клиента БЕЗ открытого вклада
    def test_negative2_calc_deposit_interest_rate(self, create_bank):
        logger = logging.getLogger("Test_logger")
        with pytest.raises(ClientDoesNotExistsError):
            create_bank.calc_deposit_interest_rate('0010')
        logger.info('Test10 info: deposit profit for client with id 0010 does not exist.')
