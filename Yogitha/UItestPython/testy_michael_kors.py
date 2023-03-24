from selenium import webdriver
# selenium is name of the file
# webdriver is the class of the file
from time import sleep
import pytest
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def set_registration_data():
    test_data_input = data_processor(3)
    input_data = test_data_input["Input"]
    input_data_array = input_data.split(",")
    firstname = input_data_array[0]
    lastname = input_data_array[1]
    email = input_data_array[2]
    password = input_data_array[3]
    confirm_password = input_data_array[4]
    zip_code = input_data_array[5]
    birth_month = input_data_array[6]
    birth_date = input_data_array[7]
    gender = input_data_array[8]
    regAccount = RegAccount()
    regAccount.set_user_details(firstname, lastname)
    regAccount.set_account_details(email, password, confirm_password, zip_code)
    regAccount.set_birth_info(birth_month, birth_date, gender)
    return regAccount


class RegAccount:
    url = "none"
    first_name = "none"
    last_name = "none"
    email_address = "none"
    password = "0"
    confirm_Password = "0"
    zip_code = "0"
    birth_month = "0"
    birth_date = "0"
    gender = "none"

    def set_url(self, url):
        self.url = url

    def set_user_details(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_account_details(self, email_address, password, confirm_password, zip_code):
        self.email_address = email_address
        self.password = password
        self.confirm_Password = confirm_password
        self.zip_code = zip_code

    def set_birth_info(self, birth_month, birth_date, gender):
        self.birth_month = birth_month
        self.birth_date = birth_date
        self.gender = gender


input_file = "test_data3.csv"
test_data_map = {}


def data_processor(test_case_id):
    with open(input_file, 'r', newline='') as csvfile:
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
    browser_me.get(test_data_input['Input'])
    title = browser_me.title
    expected_title = test_data_input['Expected_Result']
    assert expected_title in title
    browser_me.quit()


@pytest.mark.demo1
def test_case2():
    browser_me = webdriver.Edge()
    # with brackets means we are calling a function (Me) and without brackets means we are calling a variables (me)
    regAccount = set_registration_data()
    # print(test_data_input)
    browser_me.get("https://www.michaelkors.com")
    browser_me.maximize_window()
    browser_me.find_element(By.XPATH, "//*[@id='HeaderHambergerMenu']/div[5]/div[1]/div[2]/div/ul/li[2]/a").click()
    sleep(5)
    browser_me.find_element(By.XPATH, "//*[@id='first_name']").send_keys(regAccount.first_name)
    browser_me.find_element(By.XPATH, "//*[@id='last_name']").send_keys(regAccount.last_name)
    browser_me.find_element(By.XPATH, "//*[@id='email_address']").send_keys(regAccount.email_address)
    browser_me.find_element(By.XPATH, "//*[@id='postal_code']").send_keys(regAccount.zip_code)
    browser_me.find_element(By.XPATH, "//*[@id='birth_month']").send_keys(regAccount.birth_month)
    browser_me.find_element(By.XPATH, "//*[@id='birth_date']").send_keys(regAccount.birth_date)
    browser_me.find_element(By.XPATH, "//*[@id='gender_female']").click()
    # browser_me.find_element(By.XPATH, "//*[@id='create_account']/div/div[10]/div/div/div/label").click()
    browser_me.find_element(By.ID, "password").send_keys(regAccount.password)
    browser_me.find_element(By.ID, "confirm_password").send_keys(regAccount.confirm_Password)
    browser_me.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    sleep(30)
    browser_me.find_element(By.XPATH,
                            "/html/body/div[1]/div[4]/div[2]/div[3]/div/div[3]/form/div/div[11]/div/input[5]").click()

    # browser_me.quit()


@pytest.mark.demo2
def test_case3():
    browser_me = webdriver.Edge()
    browser_me.get("https://www.michaelkors.com")
    browser_me.maximize_window()
    browser_me.find_element(By.XPATH,
                            "//*[@id='HeaderHambergerMenu']/div[5]/div[1]/div[2]/div/ul/li[5]/a/span/span[1]")
    sleep(30)