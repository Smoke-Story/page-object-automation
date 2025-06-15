from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#login_link").click()
