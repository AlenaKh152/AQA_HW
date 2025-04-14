from HW21.source.HW_12_bank_deposit_21 import (Bank, ClientAlreadyExistsError,
                                               ClientDoesNotExistsError,
                                               ClientHasNoDepositError)


class BankLibrary:
    def __init__(self):
        self.bank = Bank()


    def new_client(self, client_id, name):
        try:
            return self.bank.register_client(client_id, name)
        except ClientAlreadyExistsError as e:
            return f'Клиент с id {client_id} уже зарегистрирован.'


    def get_client_name(self, client_id):
        return self.bank.clients[client_id]


    def open_deposit_accaunt(self, client_id, start_balance, years):
        try:
            return self.bank.open_deposit_accaunt(client_id, start_balance, years)
        except ClientDoesNotExistsError as e:
            return f'Клиент с id {client_id} не зарегистрирован.'


    def calculate_deposit(self, client_id):
        try:
            return self.bank.calculate_deposit(client_id)
        except ClientDoesNotExistsError as e:
            return f'Клиент с id {client_id} не зарегистрирован.'
        except ClientHasNoDepositError as e:
            return f'У клиента {client_id} отсутствуют открытые депозиты.'


    def close_deposit(self, client_id):
        try:
            return self.bank.close_deposit(client_id)
        except ClientHasNoDepositError as e:
            return f'У клиента {client_id} отсутствуют открытые депозиты.'
