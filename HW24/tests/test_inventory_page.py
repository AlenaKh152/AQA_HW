from HW24.pages.login_page import LoginPage
from HW24.pages.inventory_page import InventoryPage
from HW24.test_data.user_creds import UserCreds


# Тест позитивный: проверка наличия товаров на Inventory Page
def test_items_inventory_page_positive(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    assert inv_page.get_products_list(), 'There are no products on the Inventory Page.'


# Тест позитивный: добавление товара в корзину с Inventory Page
def test_add_item_to_cart_from_inventory_page(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    assert not inv_page.is_item_in_cart()
    add_button = inv_page.select_any_element(inv_page.add_buttons)
    add_button.click()
    assert inv_page.is_item_in_cart()


# Тест позитивный: удаление товара из корзины с Inventory Page
def test_remove_item_from_cart_from_inventory_page(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    assert not inv_page.is_item_in_cart()
    add_button = inv_page.select_any_element(inv_page.add_buttons)
    add_button.click()
    assert inv_page.is_item_in_cart()
    remove_button = inv_page.select_any_element(inv_page.remove_buttons)
    remove_button.click()
    assert not inv_page.is_item_in_cart()
