from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests
import random
import allure

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.splitlines()
word1 = str(random.choice(WORDS))
word2 = str(random.choice(WORDS))
email = word1 + word2 + "@gmail.com"

driver = webdriver.Chrome(executable_path="C:/Users/dudon/selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://automationpractice.com/index.php")

driver.find_element_by_link_text("Sign in").click()
time.sleep(2)
driver.find_element_by_id("email_create").send_keys(email)
driver.find_element_by_id("SubmitCreate").click()
WebDriverWait(driver, 5, 0.5)
driver.find_element_by_id("id_gender1").click()
driver.find_element_by_id("customer_firstname").send_keys("Valentin")
driver.find_element_by_id("customer_lastname").send_keys("Dudkevich")
driver.find_element_by_id("email").click()
driver.find_element_by_id("passwd").send_keys("V1234567")
driver.find_element_by_id("days").send_keys(u'\ue00f')
driver.find_element_by_id("days").click()
driver.find_element_by_id("months").send_keys(u'\ue00f')
driver.find_element_by_id("months").click()
driver.find_element_by_id("years").send_keys(u'\ue00f')
driver.find_element_by_id("years").click()
driver.find_element_by_id("company").send_keys("Mainsoft")
driver.find_element_by_id("address1").send_keys("St. Pol, 123")
driver.find_element_by_id("city").send_keys("Vitebsk")
driver.find_element_by_id("id_state").click()
time.sleep(2)
driver.find_element_by_id("id_state").send_keys(u'\ue00f')
driver.find_element_by_id("id_state").click()
driver.find_element_by_id("postcode").send_keys("12345")
driver.find_element_by_id("phone_mobile").send_keys("375298187090")
driver.find_element_by_id("submitAccount").click()
time.sleep(1)
driver.close()
driver.quit()
print("Test Completed")