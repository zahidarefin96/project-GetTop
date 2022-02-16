from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductPage(Page):

    ADD_TO_CART_TEXT = (By.XPATH, "//button[contains(text(),'Add to cart')]")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_TEXT)

