import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# отключаю уведомление chrome о том, что пароль был раскрыт(мешает тестам)
chr_options = Options()
chr_options.add_experimental_option("excludeSwitches", ["enable-automation", "password-leak-detection"])
chr_options.add_argument("--disable-blink-features=PasswordLeakDetection")


@pytest.fixture(autouse=True)
def create_browser():
    browser = webdriver.Chrome(options=chr_options)
    yield browser
    browser.quit()


@pytest.fixture
def login_func(create_browser):
    browser = create_browser
    browser.get("https://www.saucedemo.com/")
    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    logging_button = browser.find_element(By.ID, 'login-button')
    logging_button.click()
    yield browser
    browser.quit()


def pytest_html_report_title(report):
    report.title = "Test HW23 Saucedemo report"
