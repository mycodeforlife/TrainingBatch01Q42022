from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

# def test_case1:
driver_open = webdriver.Firefox()
driver_open.get("https://www.etsy.com/")
driver_open.maximize_window()
title = driver_open.title
print(title)
expected_title = " Shop for handmade"
assert expected_title in title

# def test_case2:
driver_open.find_element(By.XPATH, "/html/body/div[2]/header/div[4]/nav/ul/li[1]/button").click()
driver_open.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div[3]"
                                   "/div/div/div/div/div/div[2]/form/div[1]/div/div[1]/div/button").click()
driver_open.find_element(By.NAME, "email").send_keys("sajjathanuja+@gmail.com")
driver_open.find_element(By.NAME, "first_name").send_keys("thanuja")
driver_open.find_element(By.NAME, "password").send_keys("avananya@16")
driver_open.find_element(By.NAME, "submit_attempt").click()

# def test_case3:
search_bar = driver_open.find_element(By.NAME, "search_query")
driver_open.implicitly_wait(10)
search_bar.send_keys("sofa", + Keys.ENTER)
