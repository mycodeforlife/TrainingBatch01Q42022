from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]").click()
driver.implicitly_wait(5)
try:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]")
except:
    print("first name is not enter")
else:
    driver.find_element(By.NAME, "firstname").send_keys("Thanuja")
driver.find_element(By.NAME, "lastname").send_keys("Sajja")

driver.find_element(By.NAME, "reg_email__").send_keys("9256997776")
driver.find_element(By.NAME, "reg_passwd__").send_keys("avananya@16")
month = Select(driver.find_element(By.NAME, "birthday_month"))
month.select_by_visible_text("May")
day = Select(driver.find_element(By.ID, "day"))
day.select_by_visible_text("10")
year = Select(driver.find_element(By.ID, "year"))
year.select_by_visible_text("1999")
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span["
                              "1]/label").click()
driver.find_element(By.NAME, "websubmit").click()
