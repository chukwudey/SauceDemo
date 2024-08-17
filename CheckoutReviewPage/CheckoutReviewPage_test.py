import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CheckoutReviewLocator.CheckoutReviewLocator_test import CheckoutReviewLocatorPage


class CheckoutReviewPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def click_finish(self):
        click_finish = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutReviewLocatorPage.FINISH))
        click_finish.click()

        time.sleep(10)
