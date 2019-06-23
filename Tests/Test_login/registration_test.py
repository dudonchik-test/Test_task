import time
import unittest
import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Tests.Generation_email import Email
from Tests.Pages.PageRegistr import PageRegistr
from Tests.Pages.PageStart import PageStart


@allure.title ("Проверка регистрации новых пользователей")
@allure.severity(Severity.BLOCKER)
class RegistrationTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/dudon/selenium/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_registration_valid(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        sign = PageStart(driver)

        sign.Sign_in()
        WebDriverWait(driver, 40, 0.5)
        sign.Start_reg(Email())
        WebDriverWait(driver, 10, 0.5)
        sign.Start_reg1()
        WebDriverWait(driver, 10, 0.5)

        reg = PageRegistr(driver)
        WebDriverWait(driver, 10, 0.5)
        reg.gender()
        reg.firstname("Valentin")
        reg.lastname("Dudkevich")
        reg.passw("V1234567")
        reg.day(u'\ue00f')
        reg.month(u'\ue00f')
        reg.year(u'\ue00f')
        reg.company("Mainsoft")
        reg.address("St. Pol, 123")
        reg.city("Vitebsk")
        reg.state(u'\ue00f')
        reg.postcode("12346")
        reg.mobile("375298187090")
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
