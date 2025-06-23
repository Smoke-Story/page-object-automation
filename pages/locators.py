from selenium.webdriver.common.by import By

class BasePageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:

    URL_PART = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPagelocators:

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:first-child")
    LINK_PARAMETER = "promo=offer"
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_SUCCESSFUL_ADDING = (By.CSS_SELECTOR, "div.alert:first-child strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert:last-child strong")
