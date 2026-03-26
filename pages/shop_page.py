from selenium.webdriver.common.by import By

from common.base_page import BasePage


class ShopPage(BasePage):
    CHOICE = (By.XPATH,'//button[@name="add-to-cart-sauce-labs-backpack"]')
    SHOP_CART = (By.XPATH, '//a[@data-test="shopping-cart-link"]')
    CHECKOUT = (By.XPATH, '//button[@name="checkout"]')
    FIRSTNAME = (By.XPATH, '//input[@name="firstName"]')
    LASTNAME = (By.XPATH, '//input[@name="lastName"]')
    CODE = (By.XPATH, '//input[@name="postalCode"]')
    CONTINUE = (By.XPATH, '//input[@name="continue"]')

    def shop(self,firstname,lastname,code):
        self.click(self.CHOICE)
        self.click(self.SHOP_CART)
        self.click(self.CHECKOUT)
        self.input(self.FIRSTNAME,firstname)
        self.input(self.LASTNAME,lastname)
        self.input(self.CODE,code)
        self.click(self.CONTINUE)