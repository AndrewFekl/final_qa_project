from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_page_has_add_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
    assert button, "Add basket button isn't found"
