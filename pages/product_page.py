from .base_page import BasePage
from .locators import ProductPageLocators as Locators


class ProductPage(BasePage):

    def open_product_page(self, link):
        self.driver.get(link)

    def check_parameter_in_link(self):
        current_url_is = self.driver.current_url
        assert Locators.LINK_PARAMETER in current_url_is, f"{current_url_is=}"

    def add_product_to_basket_button(self):
        self.find_element_ex_wait(*Locators.ADD_TO_BASKET_BUTTON).click()

    def get_code(self):
        self.solve_quiz_and_get_code()

    def should_be_product_title_in_message(self):
        product_title = self.find_element_ex_wait(*Locators.PRODUCT_TITLE).text
        successful_adding_message = self.find_element_ex_wait(*Locators.MESSAGE_SUCCESSFUL_ADDING).text
        assert product_title == successful_adding_message, \
            "Message of successful adding product is not correct"

    def should_be_product_price_in_message(self):
        product_price = self.find_element_ex_wait(*Locators.PRODUCT_PRICE).text
        basket_price_message = self.find_element_ex_wait(*Locators.MESSAGE_BASKET_PRICE).text
        assert product_price in basket_price_message, "Total basket price is not correct"

    """Negative tests"""

    def should_not_be_success_message(self):
        success_message = self.is_not_element_present(*Locators.SUCCESS_MESSAGE)
        assert success_message, "'Success message' is appearing"

    def success_message_is_disappeared(self):
        success_message = self.is_disappeared(*Locators.SUCCESS_MESSAGE)
        assert success_message, "Success message is present"






