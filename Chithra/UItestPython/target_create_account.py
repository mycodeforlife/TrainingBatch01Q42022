import time
import csv
from selenium import webdriver
import pytest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

input_file_name = "test_data.csv"


def read_input(testcase_id):
    with(open(input_file_name, newline='')) as csvfile:
        reader = csv.DictReader(csvfile)
        for each in reader:
            if testcase_id == int(each["test_case_id"]):
                return each

# result = read_input(1)
# print(result)
@pytest.mark.test1
def test_case1():
    driver = webdriver.Firefox()
    driver.get("https://www.target.com/")
    time.sleep(10)
    browser_title = driver.title
    expected_title = "Target"
    # assert expected_title in browser_title

    # click signin
    signin_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/nav/a[4]/span")
    signin_button.click()

    # click create account
    create_account = driver.find_element(By.CSS_SELECTOR, "#listaccountNav-createAccount > a:nth-child(1) > span:nth-child(1)")
    create_account.click()
    time.sleep(10)
    driver.maximize_window()
    # enter create account details
    test_input = read_input(1)
    driver.find_element(By.ID, "username").send_keys(test_input['username'])
    driver.find_element(By.ID, "firstname").send_keys(test_input['firstname'])
    driver.find_element(By.ID, "lastname").send_keys(test_input['lastname'])
    driver.find_element(By.ID, "password").send_keys(test_input['password'])
    time.sleep(10)
    create_account = driver.find_element(By.ID, 'createAccount')
    create_account.click()
    time.sleep(10)

