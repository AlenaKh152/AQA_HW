class ClientAlreadyExistsError(Exception):
    pass


class ClientDoesNotExistsError(Exception):
    pass


class ClientHasNoDepositError(Exception):
    pass


class Bank:
    percent = 10

    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id not in self.clients:
            self.clients[client_id] = name
            print(f'Клиент с id {client_id} успешно зарегистрирован.')
            return f'Клиент с id {client_id} успешно зарегистрирован.'
        else:
            print(f'Клиент с id {client_id} уже зарегистрирован.')
            raise ClientAlreadyExistsError(f'Клиент с id {client_id} уже зарегистрирован.')

    def open_deposit_accaunt(self, client_id, start_balance, years):
        if client_id not in self.clients:
            print(f'Клиент с id {client_id} не зарегистрирован.')
            raise ClientDoesNotExistsError(f'Клиент с id {client_id} не зарегистрирован.')
        else:
            self.deposits[client_id] = [start_balance, years]
            print(f'Депозит клиента {client_id} успешно открыт.')
            return f'Депозит клиента {client_id} сумма {start_balance} срок {years} успешно открыт.'

    def calculate_deposit(self, client_id):
        result_balance = 0
        if client_id in self.deposits:
            start_sum = self.deposits[client_id][0]
            term = self.deposits[client_id][1]
            result_balance = (float(start_sum) * ((1 + (self.percent / 100) / (float(term) * 12))
                                                  ** (float(term) * 12)))
        elif client_id in self.clients and client_id not in self.deposits:
            print(f'У клиента {client_id} отсутствуют открытые депозиты.')
            raise ClientHasNoDepositError(f'У клиента {client_id} отсутствуют открытые депозиты.')
        elif client_id not in self.clients:
            print(f'Клиент с id {client_id} не зарегистрирован.')
            raise ClientDoesNotExistsError(f'Клиент с id {client_id} не зарегистрирован.')
        return round(result_balance, 2)

    def close_deposit(self, client_id):
        if client_id not in self.deposits:
            print(f'У данного клиента {client_id} отсутствуют открытые депозиты.')
            raise ClientHasNoDepositError(f'У клиента {client_id} отсутствуют открытые депозиты.')
        else:
            del self.deposits[client_id]
            print(f'Депозит клиента {self.clients[client_id]} {client_id} успешно закрыт.')
            return f'Депозит клиента {self.clients[client_id]} {client_id} успешно закрыт.'
