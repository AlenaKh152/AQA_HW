import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSauceDemo:
    #Тест позитивный: проверка входа с корректными Login и Password
    def test_user_login_positive(self, create_browser):
        browser = create_browser
        browser.get("https://www.saucedemo.com/")
        username = browser.find_element(By.ID, 'user-name')
        password = browser.find_element(By.ID, 'password')
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        logging_button = browser.find_element(By.ID, 'login-button')
        logging_button.click()
        success_text = browser.find_element(By.CLASS_NAME, 'app_logo')
        assert success_text.text == "Swag Labs"

    #Тест негативный: проверка входа с незаполненными Login и Password
    def test_user_login_negative1(self, create_browser):
        browser = create_browser
        browser.get("https://www.saucedemo.com/")
        logging_button = browser.find_element(By.ID, 'login-button')
        logging_button.click()
        error_text = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert error_text.text == "Epic sadface: Username is required"

    #Тест негативный: проверка входа с некорректными Login и Password
    def test_user_login_negative2(self, create_browser):
        browser = create_browser
        browser.get("https://www.saucedemo.com/")
        username = browser.find_element(By.ID, 'user-name')
        password = browser.find_element(By.ID, 'password')
        username.send_keys("not_standard_user")
        password.send_keys("not_secret_sauce")
        logging_button = browser.find_element(By.ID, 'login-button')
        logging_button.click()
        error_text = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert (error_text.text ==
                "Epic sadface: Username and password do not match any user in this service")

    # Тест позитивный: добавление товара в корзину
    def test_add_item_to_cart(self, login_func):
        browser = login_func
        add_button = browser.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
        add_button.click()
        cart = browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        cart.click()
        success_text = browser.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
        assert success_text.text == "Sauce Labs Backpack"

    # Тест позитивный: удаление товара из корзины
    def test_remove_item_from_cart(self, login_func):
        browser = login_func
        browser.implicitly_wait(5)
        add_button = browser.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
        add_button.click()
        cart = browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        cart.click()
        success_text = browser.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
        assert success_text.text == "Sauce Labs Backpack"
        remove_button = (WebDriverWait
                         (browser, 5).until
                         (EC.element_to_be_clickable
                          ((By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]'))))
        remove_button.click()
        success_list = browser.find_elements(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
        assert  len(success_list) == 0

    # Тест позитивный: открытие страницы карточки товара
    def test_open_item_page(self, login_func):
        browser = login_func
        item_link = browser.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
        item_link.click()
        success_text = browser.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
        assert  success_text.text == "Sauce Labs Backpack"

    # Тест позитивный: добавление нескольких товаров в корзину со страниц карточек товаров
    def test_add_items_to_cart_from_product_page(self, login_func):
        browser = login_func
        item_link1 = browser.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
        item_link1.click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'add-to-cart')))
        add_button1 = browser.find_element(By.ID, 'add-to-cart')
        add_button1.click()
        back_button = browser.find_element(By.ID, 'back-to-products')
        back_button.click()
        item_link2 = browser.find_element(By.XPATH, '//div[text()="Sauce Labs Bike Light"]')
        item_link2.click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'add-to-cart')))
        add_button2 = browser.find_element(By.ID, 'add-to-cart')
        add_button2.click()
        cart = browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        cart.click()
        success_text1 = browser.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
        success_text2 = browser.find_element(By.XPATH, '//div[text()="Sauce Labs Bike Light"]')
        assert success_text1.text == "Sauce Labs Backpack"
        assert success_text2.text == "Sauce Labs Bike Light"

    # Тест позитивный: корректное оформление заказа в корзине
    def test_complete_order_with_correct_data(self, login_func):
        browser = login_func
        add_button = browser.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
        add_button.click()
        cart = browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        cart.click()
        checkout_button = browser.find_element(By.ID, 'checkout')
        checkout_button.click()
        success_text1 = browser.find_element(By.CSS_SELECTOR, '[data-test="title"]')
        assert success_text1.text == 'Checkout: Your Information'
        first_name_field = browser.find_element(By.CSS_SELECTOR, '[data-test="firstName"]')
        first_name_field.send_keys("Tom")
        last_name_field = browser.find_element(By.CSS_SELECTOR, '[data-test="lastName"]')
        last_name_field.send_keys("Jerry")
        zipcode_name_field = browser.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]')
        zipcode_name_field.send_keys("112233")
        continue_button =  (browser.find_element
                            (By.CSS_SELECTOR, '[type="submit"][data-test="continue"]'))
        continue_button.click()
        success_text2 = browser.find_element(By.CSS_SELECTOR, '[data-test="title"]')
        assert success_text2.text == 'Checkout: Overview'
        success_text3 = browser.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
        assert success_text3.text == 'Sauce Labs Backpack'
        finish_button = browser.find_element(By.ID, 'finish')
        finish_button.click()
        success_text4 = browser.find_element(By.XPATH, '//h2[text()="Thank you for your order!"]')
        assert success_text4.text == "Thank you for your order!"

    # Тест негативный: оформление заказа в корзине c незаполненными обязательными полями
    def test_complete_order_with_incorrect_data(self, login_func):
        browser = login_func
        add_button = browser.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
        add_button.click()
        cart = browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        cart.click()
        checkout_button = browser.find_element(By.ID, 'checkout')
        checkout_button.click()
        success_text1 = browser.find_element(By.CSS_SELECTOR, '[data-test="title"]')
        assert success_text1.text == 'Checkout: Your Information'
        continue_button = (browser.find_element
                           (By.CSS_SELECTOR, '[type="submit"][data-test="continue"]'))
        continue_button.click()
        error_text1 = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert error_text1.text == 'Error: First Name is required'
        first_name_field = browser.find_element(By.CSS_SELECTOR, '[data-test="firstName"]')
        first_name_field.send_keys("Tom")
        continue_button.click()
        error_text2 = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert error_text2.text == 'Error: Last Name is required'
        last_name_field = browser.find_element(By.CSS_SELECTOR, '[data-test="lastName"]')
        last_name_field.send_keys("Jerry")
        continue_button.click()
        error_text3 = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert error_text3.text == 'Error: Postal Code is required'
        zipcode_name_field = browser.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]')
        zipcode_name_field.send_keys("112233")
        continue_button.click()
        success_text2 = browser.find_element(By.CSS_SELECTOR, '[data-test="title"]')
        assert success_text2.text == 'Checkout: Overview'
        finish_button = browser.find_element(By.ID, 'finish')
        finish_button.click()
        success_text3 = browser.find_element(By.XPATH, '//h2[text()="Thank you for your order!"]')
        assert success_text3.text == "Thank you for your order!"
