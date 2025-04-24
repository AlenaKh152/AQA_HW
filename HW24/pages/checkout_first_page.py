from HW24.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutFirstStep(BasePage):
    step_one_title = (By.CLASS_NAME, 'title')
    continue_button = (By.CLASS_NAME, 'submit-button')
    cancel_button = (By.CLASS_NAME, 'cart_cancel_link')
    first_name_field = (By.ID, 'first-name')
    last_name_field = (By.ID, 'last-name')
    zip_code_field = (By.ID, 'postal-code')
    error_text = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, browser):
        super().__init__(browser)

