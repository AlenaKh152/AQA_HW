from HW24.pages.login_page import LoginPage
from HW24.test_data.user_creds import UserCreds


# Тест позитивный: проверка входа с корректными Login и Password
def test_user_login_positive(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    assert log_page.is_logging_success(), "Logging fails, error message present"


# Тест негативный: проверка входа с незаполненными Login и Password
def test_user_login_negative1(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.empty_user, UserCreds.empty_password)
    assert not log_page.is_logging_success(), "MyFails: Logging with empty cred is correct"


# Тест негативный: проверка входа с некорректными Login и Password
def test_user_login_negative2(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.invalid_user, UserCreds.invalid_password)
    assert not log_page.is_logging_success(), "MyFails: Logging with empty cred is correct"
