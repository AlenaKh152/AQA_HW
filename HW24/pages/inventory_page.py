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

    def select_any_item_link(self):
        all_item_links = self.browser.find_elements(*self.items_links)
        return random.choice(all_item_links)

    def select_any_add_button(self):
        all_add_buttons = self.browser.find_elements(*self.add_buttons)
        return random.choice(all_add_buttons)

    def select_any_rmv_button(self):
        all_rmv_buttons = self.browser.find_elements(*self.remove_buttons)
        return random.choice(all_rmv_buttons)

