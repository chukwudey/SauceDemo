import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CheckoutLocator.CheckoutLocator_test import CheckoutLocatorPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_first_name(self, firstname):
        enter_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocatorPage.FIRSTNAME))
        enter_first_name.send_keys(firstname)

        time.sleep(5)

    def enter_last_name(self, lastname):
        enter_last_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocatorPage.LASTNAME))
        enter_last_name.send_keys(lastname)

        time.sleep(5)

    def enter_zipcode(self, zipcode):
        enter_zipcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocatorPage.ZIPCODE))
        enter_zipcode.send_keys(zipcode)

        time.sleep(5)

    def click_continue(self):
        click_continue = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocatorPage.CONTINUE))
        click_continue.click()

        time.sleep(5)