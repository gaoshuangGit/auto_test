from selenium.webdriver.common.by import By

from common.base_page import BasePage


class CartPage(BasePage):
    # FIRSTNAME = (By.ID, "first-name")
    # LASTNAME = (By.ID, "last-name")
    # CODE = (By.ID, "postal-code")
    FINISH = (By.XPATH, '//button[@id="finish"]')
    BACK = (By.XPATH, '//button[@name="back-to-products"]')


    def cart(self):
        # self.input(self.FIRSTNAME, firstname)
        # self.input(self.LASTNAME, lastname)
        # self.input(self.CODE, code)
        self.click(self.FINISH)

        self.click(self.BACK)
