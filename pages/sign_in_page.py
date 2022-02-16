from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    LOST_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Lost your password?')]")
    LOGIN_TEXT = (By.XPATH, "//h3[contains(text(),'Login')]")

    def click_lost_password_link(self):
        self.click(*self.LOST_PASSWORD_LINK)

    def verify_login_text(self):
        self.verify_text(*self.LOGIN_TEXT)
