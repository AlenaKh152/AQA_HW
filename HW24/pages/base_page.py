from selenium.common.exceptions import NoSuchElementException
from HW24.test_data.env import Env
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(Env.URL)

    def send_text(self, locator, text):
        input_field = self.browser.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)

    def click_button(self, locator, timeout=20):
        goal_button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator))
        goal_button.click()

    def find_target_element(self, locator):
        element = self.browser.find_element(*locator)
        return element

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def click_cart_button(self):
        cart_button = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart_button.click()

    def is_item_in_cart(self):
        try:
            self.browser.find_element(By. CLASS_NAME, 'shopping_cart_badge')
            return True
        except NoSuchElementException:
            return False
