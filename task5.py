test_string = input('Enter the string: ')


def is_palindrome(test_str):
    if test_str == test_str[::-1]:
        print('YES, this string is palindrome.')
    else:
        print('NO, this string is not palindrome.')


is_palindrome(test_string)
