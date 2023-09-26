from selenium import webdriver

import csv

import pytest

from selenium.webdriver.common.by import By

input_test_file = "test1.csv"


def read_input(testcase_id):
    with(open(input_test_file, newline='')) as csvfile:
        reader = csv.DictReader(csvfile)
        for each in reader:
            if testcase_id == int(each["TestCaseID"]):
                return each


class best_buy_log:
    browser = webdriver.Firefox()

    def opening_browser(self):
        input_file = read_input(1)
        self.browser.get(input_file["URL"])

    # checking the title name is correct
    @pytest.mark.demo
    def bestbuy_sign_credentials(self):
        self.opening_browser()
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        self.browser.find_element(By.XPATH, "/html/body/header/div[1]/ul[1]/li[1]/span/a")
        self.browser.find_element(By.ID, "userid").send_keys("sajjathanu@gmail.com")
        self.browser.find_element(By.ID, "signin-continue-btn").click()
        self.browser.find_element(By.ID, "pass").send_keys("avananya@16")
        self.browser.find_element(By.ID, "sgnBt").click()
