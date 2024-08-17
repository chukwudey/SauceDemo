from selenium.webdriver.common.by import By


class LogoutLocatorPage:
    HAMBURGER = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")