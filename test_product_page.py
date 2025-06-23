import pytest
from pages.product_page import ProductPage
from pages.main_page import MainPage


@pytest.mark.parametrize("parameter", [
    n if n != 7 else pytest.param(7, marks=pytest.mark.xfail) for n in range(0, 10)]) # run's 10 tests
def test_guest_can_add_product_to_basket(driver, parameter):
    link = (f"http://selenium1py.pythonanywhere.com/"
            f"catalogue/coders-at-work_207/?promo=offer{parameter}")
    product_page = ProductPage(driver)                 # присвоили класс + фикстуру
    product_page.open_product_page(link)               # открыли страницу с продуктом
    product_page.check_parameter_in_link()             # проверили параметр в ссылке
    product_page.add_product_to_basket_button()        # добавили продукт в корзину
    product_page.solve_quiz_and_get_code()             # решаем уравнение, вставляем код -> ок
    product_page.should_be_product_title_in_message()  # сверили сообщение об успешном добавлении
    product_page.should_be_product_price_in_message()  # сверили цену корзины с ценой товара

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

def test_guest_can_go_to_login_page_from_product_page(driver):
    link = ("http://selenium1py.pythonanywhere.com/"
            "en-gb/catalogue/the-city-and-the-stars_95/")
    product_page = ProductPage(driver)
    main_page = MainPage(driver)
    product_page.open_product_page(link)
    main_page.open_main_page()
