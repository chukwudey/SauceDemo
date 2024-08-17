import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from LoginLocator.LoginLocator_test import LoginLocatorPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self,username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.USERNAME))
        enter_username.send_keys(username)

        time.sleep(5)

    def enter_password(self,password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(5)

    def enter_login(self):
        enter_login = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.LOGIN))
        enter_login.click()

        time.sleep(10)