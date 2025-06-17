from .base_page import BasePage
from selenium.webdriver.common.by import By

class WebsiteLocators: # класс локаторов для удобства изпользования

    LOCATOR_LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")

class MainPage(BasePage):

    def open_main_page(self):
        self.driver.get(self.link)

    def go_to_login_page(self):
        self.find_element(WebsiteLocators.LOCATOR_LOGIN_PAGE).click()
