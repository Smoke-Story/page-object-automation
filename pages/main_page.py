from .base_page import BasePage
from .locators import MainPageLocators as Locators

class MainPage(BasePage):

    def go_to_login_page(self):
        self.find_element_exp(Locators.LOGIN_LINK, time=3).click()

    def should_be_login_link(self):
        assert self.is_element_present(*Locators.LOGIN_LINK), \
            "login link is not presented"
