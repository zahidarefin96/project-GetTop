from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART_TEXT = (By.XPATH, "//button[contains(text(),'Add to cart')]")

    IPHONE11_TEXT = (By.XPATH, "//h1[contains(text(),'iPhone 11')]")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_TEXT)

    def iphone11_text(self):
        self.verify_text(*self.IPHONE11_TEXT)
