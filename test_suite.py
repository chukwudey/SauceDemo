import time

import pytest
from selenium import webdriver

from BackHomePage.BackHomePage_test import BackHomePage
from CheckoutReviewPage.CheckoutReviewPage_test import CheckoutReviewPage
from LoginPage.LoginPage_test import LoginPage
from LogoutPage.LogoutPage_test import LogoutPage
from ProductPage.ProductPage_test import ProductPage
from CartPage.Cartpage_test import CartPage
from CheckoutPage.CheckoutPage_test import CheckoutPage
from config.config import Config, ConfigCheckout


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url(Config.BaseUrl)
    return login_page


time.sleep(5)


def test_login_page(login):
    login.enter_username(Config.Username)
    login.enter_password(Config.Password)
    login.enter_login()


def test_product_page_automation(login):
    test_product = ProductPage(login.driver)
    test_product.click_backPack()
    test_product.click_bike_light()
    test_product.select_tshirt()


def test_cart_page_automation(login):
    test_product_page = CartPage(login.driver)
    test_product_page.click_cart()
    test_product_page.click_checkout()


def test_checkout_page_automation(login):
    test_checkout_page = CheckoutPage(login.driver)
    test_checkout_page.enter_first_name(ConfigCheckout.FirstName)
    test_checkout_page.enter_last_name(ConfigCheckout.LastName)
    test_checkout_page.enter_zipcode(ConfigCheckout.ZipCode)
    test_checkout_page.click_continue()


def test_checkout_review_page_automation(login):
    test_checkout_review_page = CheckoutReviewPage(login.driver)
    test_checkout_review_page.click_finish()


def test_back_home_page_automation(login):
    test_back_home_page = BackHomePage(login.driver)
    test_back_home_page.click_back_home()

def test_logout_page_automation(login):
    test_logout_page = LogoutPage(login.driver)
    test_logout_page.click_hamburger()
    test_logout_page.click_logout()
