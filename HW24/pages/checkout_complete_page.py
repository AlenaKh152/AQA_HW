from HW24.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutCompletePage(BasePage):
    complete_title = (By.CLASS_NAME, 'title')
    back_home_button = (By.CLASS_NAME, 'btn_primary')

    def __init__(self, browser):
        super().__init__(browser)

