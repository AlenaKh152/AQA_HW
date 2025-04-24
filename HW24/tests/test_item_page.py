from HW24.pages.login_page import LoginPage
from HW24.pages.inventory_page import InventoryPage
from HW24.pages.item_page import ItemPage
from HW24.test_data.user_creds import UserCreds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест: открытие страницы карточки товара
def test_open_item_page(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    target_link = inv_page.select_any_element(inv_page.items_links)
    target_link_text = target_link.text
    target_link.click()
    item_page = ItemPage(browser)
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located(item_page.name_on_item_page))
    item_name = item_page.find_target_element(item_page.name_on_item_page)
    item_name_text = item_name.text
    assert target_link_text == item_name_text


# Тест: добавление товара в корзину со страницы карточки товара
def test_add_items_to_cart_from_product_page(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    assert not inv_page.is_item_in_cart()
    add_button = inv_page.select_any_element(inv_page.add_buttons)
    add_button.click()
    assert inv_page.is_item_in_cart()
