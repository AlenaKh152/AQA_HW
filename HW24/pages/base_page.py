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

    def send_text(self, locator, text, timeout=10):
        input_field = WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        input_field.clear()
        input_field.send_keys(text)

    def click_button(self, locator, timeout=10):
        goal_button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        goal_button.click()

    def find_target_element(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except NoSuchElementException:
            return False

    def click_cart_button(self, timeout=10):
        cb_locator = (By.CLASS_NAME, 'shopping_cart_link')
        cart_button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(cb_locator)
        )
        cart_button.click()

    def is_item_in_cart(self, timeout=10):
        try:
            badge_locator = (By. CLASS_NAME, 'shopping_cart_badge')
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(badge_locator)
            )
            return True
        except NoSuchElementException:
            return False
