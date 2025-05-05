from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    # -------------------------------
    # Locators for the login elements on the page
    # -------------------------------
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    # -------------------------------
    # Page Actions: Methods to interact with the login page elements
    # -------------------------------
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys("standard_user")

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("secret_sauce")

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
