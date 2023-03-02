import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.bestbuy.com/")
"""
driver.find_element(By.XPATH,
                    "/html/body/div[3]/div/div[1]/header/div[2]/nav/ul/li[1]/div/div/div/div/button/span").click()
time.sleep(5)
driver.find_element(By.XPATH,
                    "/html/body/div[3]/div/div[1]/header/div[2]/nav/ul/li[1]/div/div/div/div/div["
                    "1]/div/div/div/div/a[2]").click()
driver.find_element(By.ID, "firstname").send_keys("Thanuja")
driver.find_element(By.ID, "lastname").send_keys("Sajja")
"""