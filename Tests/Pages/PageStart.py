from Tests.Locators.Locators import Locators

class PageStart():

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_button = Locators.sign_in_button
        self.email_textbox = Locators.email_textbox
        self.reg_button = Locators.reg_button

    def Sign_in(self):
        self.driver.find_element_by_link_text(Locators.sign_in_button).click()

    def Start_reg(self, key):
        self.driver.find_element_by_id(Locators.email_textbox).send_keys(key)

    def Start_reg1(self):
        self.driver.find_element_by_id(Locators.reg_button).click()

    def Start_log(self, login):
        self.driver.find_element_by_id(Locators.Start_login).send_keys(login)


    def Start_pas(self, password):
        self.driver.find_element_by_id(Locators.Start_passw).send_keys(password)

    def Autoriz(self):
        self.driver.find_element_by_id(Locators.Submit_login).click()