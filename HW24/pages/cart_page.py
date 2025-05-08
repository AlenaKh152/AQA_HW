from HW24.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    cart_remove_button = (By.CSS_SELECTOR, '.btn_secondary.cart_button')
    cart_item = (By.CLASS_NAME, 'cart_item')
    cart_title = (By.CLASS_NAME, 'title')
    continue_shop_button = (By.CLASS_NAME, 'back')
    checkout_button = (By.CLASS_NAME, 'checkout_button')

    def __init__(self, browser):
        super().__init__(browser)
