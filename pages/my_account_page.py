from selenium.webdriver.common.by import By

from pages.base_page import Page


class MyAccountPage(Page):
    EMAIL_BOX = (By.CSS_SELECTOR, "#user_login")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(),'Reset password')]")

    def input_email(self):
        self.input_text('zahidarefin96@gmail.com', *self.EMAIL_BOX)

    def click_button(self):
        self.click(*self.RESET_PASSWORD_BUTTON)
