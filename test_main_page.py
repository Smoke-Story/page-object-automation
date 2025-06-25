import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_should_see_login_link(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.go_to_login_page()
        login_page = LoginPage(driver)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    page = MainPage(driver)
    page.open_main_page()
    page.go_to_basket_page()
    basket_page = BasketPage(driver)
    basket_page.should_not_be_products_in_the_basket()
    basket_page.should_be_message_that_basket_is_empty()