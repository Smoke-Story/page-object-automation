from pages.main_page import MainPage

def test_user_can_go_to_login_page(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.go_to_login_page()
