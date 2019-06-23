from Tests.Locators.Locators import Locators

class PagesClothes():

    def __init__(self, driver):
        self.driver = driver
        self.women_button = Locators.women_button
        self.list_sm = Locators.list_sm
        self.add_to_cart = Locators.add_to_cart
        self.continue_shoping = Locators.continue_shoping
        self.proceed_to_checkout = Locators.proceed_to_checkout
        self.search_query_top = Locators.search_query_top
        self.add_wishlist = Locators.add_wishlist


    def women(self):
        self.driver.find_element_by_xpath(Locators.women_button).click()

    def list_sort(self):
        self.driver.find_element_by_class_name(Locators.list_sm).click()

    def women2(self):
        self.driver.find_element_by_class_name(Locators.add_to_cart).click()

    def women3(self):
        self.driver.find_element_by_class_name(Locators.continue_shoping).click()

    def trash(self):
        self.driver.find_element_by_class_name(Locators.proceed_to_checkout).click()

    def Search(self, clothes):
        self.driver.find_element_by_id(Locators.search_query_top).send_keys(clothes)

    def searchEnter(self, tab):
        self.driver.find_element_by_id(Locators.search_query_top).send_keys(tab)

    def wishlist(self):
        self.driver.find_element_by_class_name(Locators.add_wishlist).click()