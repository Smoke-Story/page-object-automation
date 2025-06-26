import pytest
import random
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        base_page = BasePage(driver)
        base_page.open_main_page()
        base_page.go_to_login_page()
        login_page = LoginPage(driver)
        login_page.should_be_register_form()
        random_email = str(random.randint(3659, 8795)) + "rand@mail.hyz"
        random_password = 'randpass' + str(random.randint(2954, 9765))
        login_page.register_new_user(random_email, random_password)
        base_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(driver)
        product_page.open_product_page(link)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = ("http://selenium1py.pythonanywhere.com/"
                "catalogue/coders-at-work_207/?promo=offer0")
        product_page = ProductPage(driver)
        product_page.open_product_page(link)
        product_page.check_parameter_in_link()
        product_page.add_product_to_basket_button()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_product_title_in_message()
        product_page.should_be_product_price_in_message()


@pytest.mark.need_review
@pytest.mark.parametrize("part_link",
    [_ if _ != 7 else pytest.param(7, marks=pytest.mark.xfail) for _ in range(0, 10)])
def test_guest_can_add_product_to_basket(driver, part_link):
    link = (f"http://selenium1py.pythonanywhere.com/"
            f"catalogue/coders-at-work_207/?promo=offer{part_link}")
    product_page = ProductPage(driver)
    product_page.open_product_page(link)
    product_page.check_parameter_in_link()
    product_page.add_product_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_title_in_message()
    product_page.should_be_product_price_in_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver)
    product_page.open_product_page(link)
    product_page.add_product_to_basket_button()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver)
    product_page.open_product_page(link)
    product_page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver)
    product_page.open_product_page(link)
    product_page.add_product_to_basket_button()
    product_page.success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(driver):
    link = ("http://selenium1py.pythonanywhere.com/"
            "en-gb/catalogue/the-city-and-the-stars_95/")
    product_page = ProductPage(driver)
    product_page.open_product_page(link)
    product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = ("http://selenium1py.pythonanywhere.com/"
            "en-gb/catalogue/the-city-and-the-stars_95/")
    product_page = ProductPage(driver)
    main_page = MainPage(driver)
    product_page.open_product_page(link)
    main_page.open_main_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/metasploit_193/"
    product_page = ProductPage(driver)
    product_page.open_product_page(link)
    base_page = BasePage(driver)
    base_page.go_to_basket_page()
    basket_page = BasketPage(driver)
    basket_page.should_not_be_products_in_the_basket()
    basket_page.should_be_message_that_basket_is_empty()
