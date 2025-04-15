# HOMEWORK22

'''
#Login Page https://www.saucedemo.com/

1. Enter data = "standard_user" into Username field:
---> #user-name
2. Enter data = "secret_sauce" into Password field:
---> #password
3. Click to the Login button:
---> #login-button

#Main Page https://www.saucedemo.com/inventory.html

4. Add item "Sauce Labs Backpack" to cart by click to the "Add to cart" button on the Main Page:
---> [name="add-to-cart-sauce-labs-backpack"]
5. Remove item "Sauce Labs Backpack" from cart by click to the "Remove" button on the Main Page:
---> [name="remove-sauce-labs-backpack"]
6. Add item "Sauce Labs Backpack" to cart by click to the "Add to cart" button on the Main Page:
---> [name="add-to-cart-sauce-labs-backpack"]
7. Go to the Cart by clicking to the Cart icon:
---> [data-test="shopping-cart-link"]

#Cart Page https://www.saucedemo.com/cart.html

8.Remove item "Sauce Labs Backpack" from cart by click to the "Remove" button on the Cart Page:
---> [data-test="remove-sauce-labs-backpack"]
9. Go back to the Main Page by clicking to the "Continue Shopping" button:
---> .btn.btn_secondary.back.btn_medium[data-test="continue-shopping"]
10. On the Main Page Add item "Sauce Labs Backpack"
to cart by click to the "Add to cart" button:
---> [name="add-to-cart-sauce-labs-backpack"]
11. Open the Product Page by clicking to the product link "Sauce Labs Bike Light":
---> a[id="item_0_title_link"]>[data-test="inventory-item-name"]
OR
---> //div[text()="Sauce Labs Bike Light"]

#Product Page https://www.saucedemo.com/inventory-item.html?id=0

12. Click to the "Add to cart" button on the Product Page:
---> [id="add-to-cart"]
13. Click to the "Back to products" link on the Product Page:
---> [data-test="back-to-products"]
14. Go to the Cart by clicking to the Cart icon:
---> [data-test="shopping-cart-link"]
15. Click to the "Checkout" button on the Cart page:
---> #checkout

#Checkout Page step one https://www.saucedemo.com/checkout-step-one.html

16. Click to the "Cancel" button on the Checkout Page step one :
---> [data-test="cancel"]
17. Click to the "Checkout" button on the Cart page:
---> #checkout
18. Enter data = "First client" to the "First Name" field:
---> [data-test="firstName"]
19. Enter data = "Last client" to the "Last Name" field:
---> [data-test="lastName"]
20. Enter data = "111222" to the "Zip/Postal Code" field:
---> [data-test="postalCode"]
21. Click to the "Continue" button:
---> [type="submit"][data-test="continue"]

#Checkout Page step two https://www.saucedemo.com/checkout-step-two.html

22. Click to the "Finish" button on the Checkout Page step two :
---> //button[text()="Finish"]

#Checkout Complete Page https://www.saucedemo.com/checkout-step-two.html

23. Click to the "Back Home" button on the Checkout Complete Page :
---> //button[contains(@data-test, "back-to-products")]
'''
