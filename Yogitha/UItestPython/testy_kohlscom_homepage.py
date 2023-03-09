from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import csv


input_file = "test_data2.csv"
test_data_map = {}


def data_processor(test_case_id):

    with open(input_file, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for each_data in data:
            print(each_data["Test_Case"], test_case_id)
            if test_case_id == int(each_data["Test_Case"]):
                print(each_data)
                return each_data


@pytest.mark.demo
def test_case1():
    browser_me = webdriver.Edge()
    test_data_input = data_processor(1)
    print(test_data_input)
    browser_me.get(test_data_input['input'])
    title = browser_me.title
    expected_title = test_data_input['Expected_Result']
    assert expected_title in title
    browser_me.quit()


@pytest.mark.demo1
def test_case2():
    browser_me = webdriver.Edge()
    test_data_input = data_processor(2)
    print(test_data_input)
    browser_me.get(test_data_input["input"])
    browser_me.find_element(By.ID, "utility-nav").click()
    title = browser_me.title
    expected_title = test_data_input['Expected_Result']
    sleep(10)
    browser_me.quit()


@pytest.mark.demo2
def test_case3():
    browser_me = webdriver.Edge()
    test_data_input = data_processor(2)
    print(test_data_input)
    browser_me.get(test_data_input["input"])
    browser_me.find_element(By.ID, "utility-nav").click()
    sleep(5)
    browser_me.find_element(By.XPATH, "//*[@id='signInForm']/div/div[2]/button").click()
    sleep(5)
    browser_me.quit()


@pytest.mark.demo3
def test_case4():
    browser_me = webdriver.Edge()
    test_data_input = data_processor(3)
    print(test_data_input)
    browser_me.get("https://www.kohls.com")
    email_id = test_data_input["input"]
    browser_me.find_element(By.ID, "utility-nav").click()
    sleep(5)
    browser_me.find_element(By.XPATH, "//*[@id='signInForm']/div/div[2]/button").click()
    sleep(5)
    browser_me.find_element(By.XPATH, "//*[@id='input-panel1005']").send_keys(email_id)
    sleep(5)
    browser_me.quit()


@pytest.mark.demo4
def test_case5():
    browser_me = webdriver.Edge()
    test_data_input = data_processor(3)
    print(test_data_input)
    browser_me.get("https://www.kohls.com")
    input_data = test_data_input["input"]
    input_data_array = input_data.split(",")
    email_id = input_data_array[0]
    mobile = input_data_array[1]
    firstname = input_data_array[2]
    lastname = input_data_array[3]
    dob = input_data_array[4]
    password = input_data_array[5]
    confirmpassword = input_data_array[6]
    browser_me.find_element(By.ID, "utility-nav").click()
    sleep(5)
    browser_me.find_element(By.XPATH, "//*[@id='signInForm']/div/div[2]/button").click()
    sleep(5)
    browser_me.find_element(By.XPATH, "//*[@id='input-panel1005']").send_keys(email_id)
    browser_me.find_element(By.XPATH, "//*[@id='input-panel1006']").send_keys(mobile)
    browser_me.find_element(By.XPATH, "//*[@id='input-panel1007']").send_keys(firstname)
    browser_me.find_element(By.XPATH, "//*[@id='input-panel1008']").send_keys(lastname)
    browser_me.find_element(By.XPATH, "//*[@id='input-panel1010']").send_keys(dob)
    browser_me.find_element(By.XPATH, "//*[@id='input-panel1011']").send_keys(password)
    browser_me.find_element(By.XPATH, "//*[@id='input-panel1012']").send_keys(confirmpassword)
    browser_me.find_element(By.XPATH, "//*[@id='keepMeSignedIn']/div/div/div/div").click()
    sleep(3)
#browser_me.find_element(By.XPATH, "#recaptcha-anchor > div.recaptcha-checkbox-borderAnimation").click()
    sleep(5)
    #browser_me.find_element(By.ID, "button-panel1013").click()
    sleep(10)
    browser_me.quit()
