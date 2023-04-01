from selenium import webdriver
import pytest
import csv
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

input_file_name = "test_data.csv"


def read_input(testcase_id):
    with(open(input_file_name, newline='')) as csvfile:
        reader = csv.DictReader(csvfile)
        for each in reader:
            if testcase_id == int(each["test_case_id"]):
                return each


# result = read_input(2)
# print(result)

@pytest.mark.test2
def test_case2():
    driver = webdriver.Firefox()
    driver.get("https://www.target.com/")
    browser_title = driver.title
    expected_title = "Target"
    assert expected_title in browser_title

    #click signin
    signin_button = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/nav/a[4]/span")
    signin_button.click()

    #get into sign in
    signin = driver.find_element(By.CSS_SELECTOR,"#listaccountNav-signIn > a > span")
    signin.click()
    time.sleep(10)
    test_input = read_input(2)
    driver.find_element(By.ID,"username").send_keys(test_input['username'])
    driver.find_element(By.ID,"password").send_keys(test_input['password'])
    signin = driver.find_element(By.ID,"login")
    signin.click()
# skip = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div/a")
# skip.click()
# again_skip = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/div[4]/button[3]")
# again_skip.click()
