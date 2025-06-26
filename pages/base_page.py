import math
from .locators import BasePageLocators as Locators
from selenium.common.exceptions import NoAlertPresentException
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, imp_wait=3):
        self.driver = driver
        # self.driver.implicitly_wait(imp_wait)
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.link_login_page = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    # тестовые методы для статичных блоков сайта. Используются в файлах test_***
    def open_main_page(self):
        self.driver.get(self.link)

    def go_to_login_page(self):
        self.find_element_ex_wait(*Locators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*Locators.LOGIN_LINK), \
            "login link is not presented"
    def go_to_basket_page(self):
        self.find_element_ex_wait(*Locators.BASKET_LINK).click()

    def current_language(self):
        return self.driver.find_element(*Locators.LANGUAGE_ELEMENT).get_attribute("lang")

    def should_be_authorized_user(self):
        self.is_element_present(*Locators.USER_ICON), "User is not authorized."

    # Вспомогательные методы

    def find_element_ex_wait(self, method, selector, timeout=4):  # поиск с явным ожиданием
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((method, selector)), f"Element can't be detected by {selector}")

    def is_element_present(self, method, selector):
        try:
            self.driver.find_element(method, selector)
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, method, selector, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((method, selector)), f"Element {selector} is present")
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, method, selector, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1).until_not(
                EC.presence_of_element_located((method, selector)), f"Element {selector} is not disappeared")
        except TimeoutException:
            return False

        return True

    # Метод решающий уравнение и отвечающий на alert
    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()