from selenium.webdriver.common.keys import Keys

from Tests.Pages.PagesClothes import PagesClothes
import time
import unittest
import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Tests.Pages.PageStart import PageStart


@allure.title ("Тестирование работы поиска/ добавление товара в wishlist")
@allure.severity(Severity.BLOCKER)
class SearchTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/dudon/selenium/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        sign = PageStart(driver)
        sign.Sign_in()
        WebDriverWait(driver, 40, 0.5)
        sign.Start_log("V123@gmail.com")
        sign.Start_pas("V1234567")
        sign.Autoriz()
        WebDriverWait(driver, 40, 0.5)
        shop = PagesClothes(driver)
        shop.Search("dress")
        shop.searchEnter(Keys.ENTER)
        WebDriverWait(driver, 40, 0.5)
        shop.list_sort()
        WebDriverWait(driver, 40, 0.5)
        shop.wishlist()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")