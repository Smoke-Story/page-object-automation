from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, imp_waits=5):

        self.driver = driver
        self.driver.implicitly_wait(imp_waits)
        self.link = "http://selenium1py.pythonanywhere.com/"

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), f"Can't find element by {locator}")
