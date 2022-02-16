from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    IPHONE_SE = (By.LINK_TEXT, "iPhone SE")

    def verify_iphone_se_text(self):
        self.verify_text(*self.IPHONE_SE)
