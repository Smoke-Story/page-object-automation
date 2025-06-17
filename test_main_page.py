from pages.main_page import MainPage

def test_guest_can_go_to_login_page(driver):

    page = MainPage(driver)
    page.open_main_page()
    page.go_to_login_page()


def test_guest_should_see_login_link(driver):

    page = MainPage(driver)
    page.open_main_page()
    page.should_be_login_link()
