from HW24.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    username = (By.ID, 'user-name')
    password = (By.ID, 'password')
    logging_button = (By.ID, 'login-button')
    error_message = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, browser):
        super().__init__(browser)

    def complete_login(self, user_name, pass_word):
        self.send_text(self.username, user_name )
        self.send_text(self.password, pass_word)
        self.click_button(self.logging_button)

    def is_logging_success(self):
        return not self.is_element_present(self.error_message)

