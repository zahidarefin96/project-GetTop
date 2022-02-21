from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    # tmtn-133
    IPHONE = (By.XPATH, "//p[contains(text(),'iPhone')]")
    QUICK_VIEW_TEXT = (By.XPATH,
                       "//body/div[@id='wrapper']/main[@id='main']/div[@id='content']/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/a[1]")
    CART_ICON = (By.XPATH, "//strong[@xpath='1']")

    # tmtn-102
    USER_ICON = (By.XPATH, "//i[@class='icon-user']")

    # tmtn-123
    SEARCH_ICON1 = (By.XPATH, "//a//i[@class='icon-search']")
    SEARCH_ICON2 = (By.XPATH, "//form//div//button//i[@xpath='1']")
    INPUT_BOX = (By.XPATH, "//input[@id='woocommerce-product-search-field-0']")
    PHONES = (By.XPATH, "//div[@class='autocomplete-suggestion']")

    def hover_lang(self):
        iphone = self.find_element(*self.IPHONE)
        self.driver.execute_script("arguments[0].scrollIntoView();", iphone)
        actions = ActionChains(self.driver)
        actions.move_to_element(iphone)
        actions.perform()

    def click_quick_view(self):
        self.click(*self.QUICK_VIEW_TEXT)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_icon(self):
        self.click(*self.USER_ICON)

    def search_icon1(self):
        self.click(*self.SEARCH_ICON1)

    def input_box(self):
        self.input_text('iphone 11', *self.INPUT_BOX)
        phones = self.driver.find_elements(*self.PHONES)
        for phone in phones:
            if phone.text == "iPhone 11":
                phone.click()
                break
