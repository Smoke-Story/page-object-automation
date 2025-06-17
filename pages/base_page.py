from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, imp_wait=3):
        self.driver = driver
        self.driver.implicitly_wait(imp_wait)
        self.link = "http://selenium1py.pythonanywhere.com/"

    def open_main_page(self):
        self.driver.get(self.link)

    def find_element_exp(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), f"element can't be detected by {locator}")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

