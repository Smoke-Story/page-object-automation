from .base_page import BasePage
from selenium.webdriver.common.by import By

class WebsiteLocators:
    LOCATOR_LOGIN_LINK_EXW = (By.CSS_SELECTOR, "#login_link")
    LOCATOR_LOGIN_LINK = "#login_link"


class MainPage(BasePage):

    def go_to_login_page(self):
        self.find_element_exp(WebsiteLocators.LOCATOR_LOGIN_LINK_EXW, time=3).click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, WebsiteLocators.LOCATOR_LOGIN_LINK), \
            "login link is not presented"
