from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    ADD_TO_CART_TEXT = (By.CSS_SELECTOR, "div.message-container.container.success-color.medium-text-center")

    def verify_iphone_se_text(self):
        self.verify_text('“iPhone SE” has been added to your cart.', *self.ADD_TO_CART_TEXT)
