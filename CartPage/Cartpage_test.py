import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CartLocator.CartLocator_test import CartLocatorPage


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def click_cart(self):
        click_cart = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CartLocatorPage.CART))
        click_cart.click()

        time.sleep(5)

    def click_checkout(self):
        click_checkout = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CartLocatorPage.CHECKOUT))
        click_checkout.click()
        time.sleep(5)
