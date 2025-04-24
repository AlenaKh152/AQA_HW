from HW24.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutSecondStep(BasePage):
    step_two_title = (By.CLASS_NAME, 'title')
    cancel_button = (By.CLASS_NAME, 'cart_cancel_link')
    finish_button = (By.CLASS_NAME, 'btn_action')

    def __init__(self, browser):
        super().__init__(browser)
