from selenium.webdriver.common.by import By

from common.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH,'//input[@placeholder="Username"]')
    PASSWORD = (By.XPATH, '//input[@placeholder="Password"]')
    BUTTON = (By.XPATH, '//input[@type="submit"]')

    def login(self):
        self.input(self.USERNAME,"standard_user")
        self.input(self.PASSWORD,"secret_sauce")
        self.click(self.BUTTON)