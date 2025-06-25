from .base_page import BasePage
from .locators import LoginPageLocators as Locators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert Locators.URL_PART in self.driver.current_url, \
            f"Current url is {self.driver.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*Locators.LOGIN_FORM), \
            f"Can't find element by {Locators.LOGIN_FORM}"

    def should_be_register_form(self):
        assert self.is_element_present(*Locators.REGISTER_FORM), \
            f"Can't find element by {Locators.REGISTER_FORM}"

    def register_new_user(self, email, password):
        self.driver.find_element(*Locators.REGISTER_EMAIL).send_keys(email)
        self.driver.find_element(*Locators.REGISTER_PASSWORD1).send_keys(password)
        self.driver.find_element(*Locators.REGISTER_PASSWORD2).send_keys(password)
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
