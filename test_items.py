import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestLan:
    def test_button(selfs, browser):
        browser.get(link)
        time.sleep(5)

        assert browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')