import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ProductLocators.ProductLoctors_test import ProductLocatorPage


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def click_backPack(self):
        click_backpack = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ProductLocatorPage.BACKPACK))
        click_backpack.click()

        time.sleep(5)

    def click_bike_light(self):
        click_bike_light = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ProductLocatorPage.BIKE_LIGHT))
        click_bike_light.click()

        time.sleep(5)

    def select_tshirt(self):
        select_tshirt = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ProductLocatorPage.T_SHIRT))
        select_tshirt.click()

        time.sleep(5)


