import os
from typing import Any

os.system('cls')


class Bank:
    percent = 10

    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        self.clients[client_id] = name

    def open_deposit_accaunt(self, client_id, start_balance, years):
        if client_id not in self.clients:
            print('Клиент не зарегистрирован.')
        else:
            self.deposits[client_id] = [start_balance, years]

    def calc_deposit_interest_rate(self, client_id):
        result_balance = 0
        if client_id in self.deposits:
            start_sum = self.deposits[client_id][0]
            term = self.deposits[client_id][1]
            result_balance = start_sum * ((1 + (self.percent / 100) / (term * 12)) ** (term * 12))
        elif client_id in self.clients and client_id not in self.deposits:
            print(f'У клиента {self.clients[client_id]} отсутствуют открытые депозиты.')
        elif client_id not in self.clients:
            print('Клиент с данным id не зарегистрирован.')
        return round(result_balance, 2)

    def close_deposit(self, client_id):
        if client_id not in self.deposits:
            print('У данного клиента отсутствуют открытые депозиты.')
        else:
            del self.deposits[client_id]
            print(f'Депозит клиента {self.clients[client_id]} успешно удален.')


bank = Bank()

bank.register_client('0001', 'Alena')
bank.register_client('0002', 'Yura')

bank.open_deposit_accaunt('0001', 1000, 1)
bank.open_deposit_accaunt('0002', 2000, 2)

bank.calc_deposit_interest_rate('0003')

bank.close_deposit('0002')

print(bank.calc_deposit_interest_rate('0001'))

if __name__ == '__main__':
    assert bank.calc_deposit_interest_rate('0001') == 1104.72, "<My Err message: Incorrect result>"
# print(bank.calc_deposit_interest_rate('0001'))
