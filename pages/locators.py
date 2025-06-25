from selenium.webdriver.common.by import By

class BasePageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LANGUAGE_ELEMENT = (By.CSS_SELECTOR, "html")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:

    URL_PART = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:first-child")
    LINK_PARAMETER = "promo=offer"
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_SUCCESSFUL_ADDING = (By.CSS_SELECTOR, "div.alert:first-child strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert:last-child strong")


class BasketPageLocators:

    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

