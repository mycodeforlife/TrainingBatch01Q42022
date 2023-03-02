from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# def ebay_homepage():
driver_open = webdriver.Firefox()
driver_open.get("https://ebay.com")
driver_open.find_element(By.XPATH, "/html/body/header/div[1]/ul[1]/li[1]/span/a")
driver_open.find_element(By.ID, "userid").send_keys("sajjathanu@gmail.com")
driver_open.find_element(By.ID, "signin-continue-btn").click()
driver_open.find_element(By.ID, "pass").send_keys("avananya@16")
driver_open.find_element(By.ID, "sgnBt").click()
web_element = driver_open.find_element(By.ID, "gh-ac")
driver_open.implicitly_wait(10)
web_element.send_keys("sofa", + Keys.ENTER)