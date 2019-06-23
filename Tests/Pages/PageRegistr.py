from Tests.Locators.Locators import Locators


class PageRegistr():

    def __init__(self, driver):
        self.driver = driver
        self.gender_check = Locators.gender_check
        self.firstname_textbox = Locators.firstname_textbox
        self.lastname_textbox = Locators.lastname_textbox
        self.email_check = Locators.email_check
        self.passwd_textbox = Locators.passwd_textbox
        self.day_check = Locators.day_check
        self.month_check = Locators.month_check
        self.year_check = Locators.year_check
        self.company_textbox = Locators.company_textbox
        self.address_textbox1 = Locators.address_textbox1
        self.city_textbox = Locators.city_textbox
        self.state_check = Locators.state_check
        self.postcode_textbox = Locators.postcode_textbox
        self.phone_mobile_textbox = Locators.phone_mobile_textbox
        self.submit_account_button = Locators.submit_account_button

    def gender(self):
        self.driver.find_element_by_id(Locators.gender_check).click()

    def firstname(self, name):
        self.driver.find_element_by_id(Locators.firstname_textbox).send_keys(name)

    def lastname(self, fam):
        self.driver.find_element_by_id(Locators.lastname_textbox).send_keys(fam)
        self.driver.find_element_by_id(Locators.email_check).click()

    def passw(self, paswd):
        self.driver.find_element_by_id(Locators.passwd_textbox).send_keys(paswd)

    def day(self, key):
        self.driver.find_element_by_id(Locators.day_check).send_keys(key)
        self.driver.find_element_by_id(Locators.day_check).click()

    def month(self, key):
        self.driver.find_element_by_id(Locators.month_check).send_keys(key)
        self.driver.find_element_by_id(Locators.month_check).click()

    def year(self, key):
        self.driver.find_element_by_id(Locators.year_check).send_keys(key)
        self.driver.find_element_by_id(Locators.year_check).click()
    def company(self, comp):
        self.driver.find_element_by_id(Locators.company_textbox).send_keys(comp)

    def address(self, addr):
        self.driver.find_element_by_id(Locators.address_textbox1).send_keys(addr)

    def city(self, cities):
        self.driver.find_element_by_id(Locators.city_textbox).send_keys(cities)
        self.driver.find_element_by_id(Locators.state_check).click()

    def state(self, key):
        self.driver.find_element_by_id(Locators.state_check).send_keys(key)
        self.driver.find_element_by_id(Locators.state_check).click()

    def postcode(self, code):
        self.driver.find_element_by_id(Locators.postcode_textbox).send_keys(code)

    def mobile(self, mobile_phone):
        self.driver.find_element_by_id(Locators.phone_mobile_textbox).send_keys(mobile_phone)
        self.driver.find_element_by_id(Locators.submit_account_button).click()
