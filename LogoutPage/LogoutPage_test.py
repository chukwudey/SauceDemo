import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from LogoutLocator.LogoutLocator_test import LogoutLocatorPage


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def click_hamburger(self):
        click_hamburger = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutLocatorPage.HAMBURGER))
        click_hamburger.click()

        time.sleep(5)

    def click_logout(self):
        click_logout = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutLocatorPage.LOGOUT))
        click_logout.click()

        time.sleep(5)