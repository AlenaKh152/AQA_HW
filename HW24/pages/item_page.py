from HW24.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ItemPage(BasePage):
    add_button = (By.ID, 'add-to-cart')
    item_title = (By.CLASS_NAME, 'inventory_details_name')
    remove_button = (By.ID, 'remove')
    name_on_item_page = (By.CLASS_NAME, 'inventory_details_name')

    def __init__(self, browser):
        super().__init__(browser)
