from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.sign_in_page import SignInPage
from pages.my_account_page import MyAccountPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.cart_page = CartPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.my_account_page = MyAccountPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)


