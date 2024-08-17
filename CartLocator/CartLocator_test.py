from selenium.webdriver.common.by import By

class CartLocatorPage :
    CART = (By.XPATH, "//a[@class='shopping_cart_link']")
    CHECKOUT = (By.XPATH,"//button[@id='checkout']")