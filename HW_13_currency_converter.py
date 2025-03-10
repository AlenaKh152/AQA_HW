import os
os.system('cls')


class Person:
    def __init__(self, from_currency, amount):
        self.from_currency = from_currency
        self.amount = amount


class CurrencyConverter:
    rates = {'USD' : 3.269, 'EUR' : 3.52}

    def exchange_currency(self, person, to_currency='BYN'):
        if to_currency == 'BYN':
            total = person.amount * self.rates[person.from_currency]
        else:
            total = person.amount * (self.rates[person.from_currency] / self.rates[to_currency])
        return round(total, 2), to_currency


vasya = Person('USD', 10)
petya = Person('EUR', 10)

converter = CurrencyConverter()

print(converter.exchange_currency(vasya))
print(converter.exchange_currency(vasya))

print(converter.exchange_currency(vasya, 'EUR'))
print(converter.exchange_currency(petya, 'USD'))

if __name__ == '__main__':
    assert converter.exchange_currency(vasya) == (32.69, "BYN"), '<MyErr: wrong result>'
    assert converter.exchange_currency(petya) == (35.20, "BYN"), '<MyErr: wrong result>'
    assert converter.exchange_currency(vasya, 'EUR') == (9.29, "EUR"), '<MyErr: wrong result>'
    assert converter.exchange_currency(petya, 'USD') == (10.77, "USD"), '<MyErr: wrong result>'
