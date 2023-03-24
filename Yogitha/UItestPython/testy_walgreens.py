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
    phone = input_data_array[4]
    zip = input_data_array[5]
    regAccount = RegAccount()
    regAccount.set_user_details(firstname, lastname)
    regAccount.set_account_details(email, password, phone, zip)
    return regAccount


class RegAccount:
    url = "none"
    first_name = "none"
    last_name = "none"
    email_address = "none"
    password = "0"
    phone = "0"
    zip = "0"

    def set_url(self, url):
        self.url = url

    def set_user_details(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_account_details(self, email_address, password, phone, zip_code):
        self.email_address = email_address
        self.password = password
        self.phone = phone
        self.zip = zip_code


input_file = "test_wal.csv"
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
    browser_me.get("https://www.walgreens.com")
    browser_me.maximize_window()
    browser_me.find_element(By.XPATH,
                            "/html/body/header/div[1]/nav/div/div/div[4]/div[1]/a/span[2]/div[2]/strong").click()
    sleep(5)
    browser_me.find_element(By.XPATH, "//*[@id='pf-dropdown-register']/strong").click()
    browser_me.find_element(By.NAME, "firstName").send_keys(regAccount.first_name)
    browser_me.find_element(By.NAME, "lastName").send_keys(regAccount.last_name)
    browser_me.find_element(By.NAME, "registerData").send_keys(regAccount.email_address)
    browser_me.find_element(By.XPATH, "//*[@id='wag-password']").send_keys(regAccount.password)
    browser_me.find_element(By.XPATH, "//*[@id='wag-showpassword-checkbox']").click()
    browser_me.find_element(By.XPATH, "//*[@id='wag-reg-myw-checkbox']").click()
    sleep(5)
    # browser_me.find_element(By.XPATH, "/html").click()
    sleep(5)
    browser_me.find_element(By.NAME, "phoneno").send_keys(regAccount.phone)
    sleep(10)
    browser_me.find_element(By.XPATH, "//*[@id='wag-mywUser-zipcode']").send_keys(regAccount.zip)
    sleep(5)
    # browser_me.find_element(By.XPATH, "//*[@id='wag-mywterms-checkbox']").click()
    sleep(5)


@pytest.mark.demo2
def test_case3():
    browser_me = webdriver.Edge()
    browser_me.get("https://www.walgreens.com")
    browser_me.maximize_window()
    browser_me.find_element(By.XPATH, "//*[@id='ntt-placeholder']").click()
    sleep(5)
    browser_me.find_element(By.XPATH, "//*[@id='ntt-placeholder']").send_keys("tylenol kids")
    sleep(5)
    browser_me.find_element(By.XPATH, "//*[@id='bindval']").click()
    sleep(5)
    browser_me.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    sleep(5)
    browser_me.find_element(By.NAME, "pickup-ship-btn").click()
    sleep(5)
    browser_me.find_element(By.XPATH,
                            "/html/body/div[15]/div/div/div[1]/div/form/fieldset/div[1]/label/div/span[2]/h3").click()
    sleep(10)
    browser_me.find_element(By.XPATH, "//*[@id='addToCart-cart-checkout']/span").click()
    sleep(10)
    browser_me.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    sleep(5)
    browser_me.find_element(By.ID, "wag-cart-proceed-to-checkout").click()
    sleep(10)
    browser_me.quit()
