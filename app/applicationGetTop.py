from pages.cart_page import Cart
from pages.main_page import Main
from pages.product_page import Product


class ApplicationGettop:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = Main(self.driver)
        self.product_page = Product(self.driver)
        self.cart_page = Cart(self.driver)
