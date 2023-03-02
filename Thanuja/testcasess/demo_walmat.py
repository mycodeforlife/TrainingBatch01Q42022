from selenium import webdriver
from selenium.webdriver.common.by import By

# def test_case1:
driver_open = webdriver.Firefox()
driver_open.get("https://www.walmart.com")
driver_open.maximize_window()
title = driver_open.title
print(title)
expected_title = "Walmart.com"
assert expected_title in title

# def test_case2:
driver_open.find_element(By.XPATH, "/html/body/div/div[1]/div/span/header/div[3]/a/div/div[2]").click()
driver_open.find_element(By.XPATH, "/html/body/div/div[1]/div/span/header/div[3]/div/div/button").click()
driver_open.find_element(By.NAME, "Email Address")
driver_open.find_element(By.XPATH, "/html/body/div/div[1]/section/form/button").click()
driver_open.find_element(By.NAME, "firstName").send_keys("thanuja")
driver_open.find_element(By.XPATH, "lastName").send_keys("sajja")
driver_open.find_element(By.NAME, "newPassword").send_keys("Avananya@16")
driver_open.find_element(By.NAME, "Create Account").click()

# def test_case3:
search_element = driver_open.find_element(By.XPATH, "/html/body/div/div[1]/div/span/header/form/div/input")
search_element.send_keys("kids bike")
driver_open.find_element(By.XPATH, "/html/body/div/div[1]/div/span/header/form/div/button[2]/i").click()





