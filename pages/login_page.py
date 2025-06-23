from .base_page import BasePage
from .locators import LoginPageLocators as Locators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    # реализация этих трёх методов:
    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert Locators.URL_PART in self.driver.current_url, \
            f"Current url is {self.driver.current_url}"

    def should_be_login_form(self):
        # проверка что на странице есть форма логина
        assert self.is_element_present(*Locators.LOGIN_FORM), \
            f"Can't find element by {Locators.LOGIN_FORM}"

    def should_be_register_form(self):
        # проверка что на странице есть форма регистрации
        assert self.is_element_present(*Locators.REGISTER_FORM), \
            f"Can't find element by {Locators.REGISTER_FORM}"
