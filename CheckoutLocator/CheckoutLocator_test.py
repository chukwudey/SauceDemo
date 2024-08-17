from selenium.webdriver.common.by import By


class CheckoutLocatorPage:
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIPCODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
