test_str = 'This is my test string 123456789'
first_symbol = test_str[0]
last_symbol = test_str[-1]
third_symbol = test_str[2]
pre_third_symbol = test_str[-3]
str_len = len(test_str)
rev_str = test_str[::-1]
to_eight_symbols = test_str[:9]

print(f'Test string: {test_str}\nFirst symbol: {first_symbol}\nLast symbol: {last_symbol}\n'
      f'Third symbol: {third_symbol}\nThird from the end symbol: {pre_third_symbol}\n'
      f'String length: {str_len}\nReversed string: {rev_str}\nFirst 8 symbols: {to_eight_symbols}')
