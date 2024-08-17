import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from BackHomeLocator.BackHomeLocator_test import BackHomeLocatorPage


class BackHomePage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def click_back_home(self):
        click_back_home = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(BackHomeLocatorPage.BACK_HOME))
        click_back_home.click()

        time.sleep(5)
