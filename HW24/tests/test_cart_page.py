from HW24.pages.login_page import LoginPage
from HW24.pages.inventory_page import InventoryPage
from HW24.pages.cart_page import CartPage
from HW24.pages.checkout_first_page import CheckoutFirstStep
from HW24.pages.checkout_second_page import CheckoutSecondStep
from HW24.pages.checkout_complete_page import CheckoutCompletePage
from HW24.test_data.user_creds import UserCreds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест: открытие страницы корзины
def test_open_cart_page(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    inv_page.click_cart_button()
    cart_page = CartPage(browser)
    assert cart_page.is_element_present(cart_page.cart_title), 'Cart page is not opened'


# Тест: добавление товара в корзину
def test_add_item_to_cart(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    add_button = inv_page.select_any_element(inv_page.add_buttons)
    add_button.click()
    inv_page.click_cart_button()
    cart_page = CartPage(browser)
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located(cart_page.cart_item))
    assert cart_page.is_element_present(cart_page.cart_item)


# Тест: удаление товара из корзины
def test_delete_item_from_cart(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    add_button = inv_page.select_any_element(inv_page.add_buttons)
    add_button.click()
    inv_page.click_cart_button()
    cart_page = CartPage(browser)
    cart_page.click_button(cart_page.cart_remove_button)
    assert not cart_page.is_element_present(cart_page.cart_item)


# Тест: возврат к Inventory Page из корзины
def test_continue_shopping(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    inv_page.click_cart_button()
    cart_page = CartPage(browser)
    cart_page.click_button(cart_page.continue_shop_button)
    inv_page_new = InventoryPage(browser)
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located
                                     (inv_page_new.inventory_page_title))
    assert inv_page_new.is_element_present(inv_page_new.inventory_page_title)


# Тест: корректное оформление заказа в корзине
def test_complete_order_with_correct_data(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    add_button = inv_page.select_any_element(inv_page.add_buttons)
    add_button.click()
    inv_page.click_cart_button()
    cart_page = CartPage(browser)
    cart_page.click_button(cart_page.checkout_button)
    checkout_f_page = CheckoutFirstStep(browser)
    checkout_f_page.send_text(checkout_f_page.first_name_field, 'Test First Name')
    checkout_f_page.send_text(checkout_f_page.last_name_field, 'Test Last Name')
    checkout_f_page.send_text(checkout_f_page.zip_code_field, '112233')
    checkout_f_page.click_button(checkout_f_page.continue_button)
    checkout_s_page = CheckoutSecondStep(browser)
    checkout_s_page.click_button(checkout_s_page.finish_button)
    checkout_complete_page = CheckoutCompletePage(browser)
    assert checkout_complete_page.is_element_present(checkout_complete_page.complete_title)


# Тест: оформление заказа в корзине c незаполненными обязательными полями
def test_complete_order_with_incorrect_data(browser):
    log_page = LoginPage(browser)
    log_page.open()
    log_page.complete_login(UserCreds.valid_user, UserCreds.valid_password)
    inv_page = InventoryPage(browser)
    add_button = inv_page.select_any_element(inv_page.add_buttons)
    add_button.click()
    inv_page.click_cart_button()
    cart_page = CartPage(browser)
    cart_page.click_button(cart_page.checkout_button)
    checkout_f_page = CheckoutFirstStep(browser)
    checkout_f_page.click_button(checkout_f_page.continue_button)
    error1 = checkout_f_page.find_target_element(checkout_f_page.error_text)
    assert error1.text == 'Error: First Name is required'
    checkout_f_page.send_text(checkout_f_page.first_name_field, 'Test First Name')
    checkout_f_page.click_button(checkout_f_page.continue_button)
    error2 = checkout_f_page.find_target_element(checkout_f_page.error_text)
    assert error2.text == 'Error: Last Name is required'
    checkout_f_page.send_text(checkout_f_page.last_name_field, 'Test Last Name')
    checkout_f_page.click_button(checkout_f_page.continue_button)
    error3 = checkout_f_page.find_target_element(checkout_f_page.error_text)
    assert error3.text == 'Error: Postal Code is required'
    checkout_f_page.send_text(checkout_f_page.zip_code_field, '112233')
    checkout_f_page.click_button(checkout_f_page.continue_button)
    checkout_s_page = CheckoutSecondStep(browser)
    checkout_s_page.click_button(checkout_s_page.finish_button)
    checkout_complete_page = CheckoutCompletePage(browser)
    assert checkout_complete_page.is_element_present(checkout_complete_page.complete_title)
