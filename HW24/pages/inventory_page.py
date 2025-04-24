from HW24.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import random


class InventoryPage(BasePage):
    add_buttons = (By.CLASS_NAME, 'btn_primary')
    remove_buttons = (By.CLASS_NAME, 'btn_secondary')
    items_links = (By.CLASS_NAME, 'inventory_item_name')
    inv_items = (By.CSS_SELECTOR, '[data-test = "inventory-item"]')
    inventory_page_title = (By.CLASS_NAME, 'title')

    def __init__(self, browser):
        super().__init__(browser)

    def get_products_list(self):
        p_elements = self.browser.find_elements(*self.inv_items)
        if len(p_elements) > 0:
            return True
        else:
            return False

    def select_any_element(self, locator):
        all_items = self.browser.find_elements(*locator)
        return random.choice(all_items)
