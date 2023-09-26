from selenium import webdriver
from selenium.webdriver.common.by import By

# def ebay_homepage():
driver_open = webdriver.Firefox()
driver_open.get("https://www.ebay.com/")
driver_open.find_element(By.XPATH, "/html/body/header/div[1]/ul[1]/li[1]/span/span/a").click()
driver_open.implicitly_wait(5)
driver_open.find_element(By.ID, "personalaccount-radio").click()
driver_open.find_element(By.ID, "firstname").send_keys("Thanuja")
driver_open.find_element(By.ID, "lastname").send_keys("sajja")
driver_open.find_element(By.ID, "Email").send_keys("sajjathanu@gmail.com")
driver_open.find_element(By.ID, "password").send_keys("avananya@16")
driver_open.find_element(By.ID, "EMAIL_REG_FORM_SUBMIT").click()
