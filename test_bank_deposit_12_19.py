import unittest
from HW_12_bank_deposit import Bank

import os
os.system('cls')


class TestBank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = Bank()


    # Тест позитивный: регистрация клиента
    def test_positive_register_client(self):
        TestBank.bank.register_client('0001', 'Alena')
        self.assertTrue(TestBank.bank.clients['0001'] == 'Alena')


    # Тест негативный: регистрация клиента
    def test_negative_register_client(self):
        TestBank.bank.register_client('0002', 'Alena')
        TestBank.bank.register_client('0002', 'Anton')
        self.assertFalse(TestBank.bank.clients['0002'] == 'Anton')


    # Тест позитивный: открытие депозита для зарегистрированного клиента
    def test_positive_open_deposit_account(self):
        TestBank.bank.register_client('0003', 'Alena')
        TestBank.bank.open_deposit_accaunt('0003', 2000, 2)
        self.assertTrue(TestBank.bank.deposits['0003'] == [2000, 2])


    # Тест негативный: открытие депозита для НЕ зарегистрированного клиента
    def test_negative_open_deposit_account(self):
        TestBank.bank.open_deposit_accaunt('0004', 2000, 2)
        self.assertNotIn('0004', TestBank.bank.deposits)


    # Тест позитивный: закрытие депозита для зарегистрированного клиента
    def test_positive_close_deposit(self):
        TestBank.bank.register_client('0005', 'Alena')
        TestBank.bank.open_deposit_accaunt('0005', 2000, 2)
        TestBank.bank.close_deposit('0005')
        self.assertNotIn('0005', TestBank.bank.deposits)


    # Тест негативный: закрытие не открытого депозита для зарегистрированного клиента
    def test_negative1_close_deposit(self):
        TestBank.bank.register_client('0006', 'Alena')
        TestBank.bank.close_deposit('0006')
        self.assertNotIn('0006', TestBank.bank.deposits)


    # Тест негативный: закрытие не открытого депозита для НЕ зарегистрированного клиента
    def test_negative2_close_deposit(self):
        TestBank.bank.close_deposit('0007')
        self.assertNotIn('0007', TestBank.bank.deposits)


    # Тест позитивный: подсчет профита депозита для зарегистрированного клиента с открытым вкладом
    def test_positive_calc_deposit_interest_rate(self):
        TestBank.bank.register_client('0008', 'Alena')
        TestBank.bank.open_deposit_accaunt('0008', 1000, 1)
        self.assertEqual(TestBank.bank.calc_deposit_interest_rate('0008'), 1104.71)


    # Тест негативный: подсчет профита депозита для зарегистрированного клиента БЕЗ открытого вклада
    def test_negative1_calc_deposit_interest_rate(self):
        TestBank.bank.register_client('0009', 'Alena')
        self.assertEqual(TestBank.bank.calc_deposit_interest_rate('0009'), 0)


    # Тест негативный: подсчет профита депозита для НЕ зарегистрированного клиента БЕЗ открытого вклада
    def test_negative2_calc_deposit_interest_rate(self):
        self.assertEqual(TestBank.bank.calc_deposit_interest_rate('0010'), 0)


if __name__ == '__main__':
    unittest.main()
