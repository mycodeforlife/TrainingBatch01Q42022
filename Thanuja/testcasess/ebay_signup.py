
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
    def bestbuy_url_page(self):
        self.opening_browser()
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        get_title = self.browser.title
        assert "Ebay" in get_title
        self.browser.quit()

    def test_case2(self):
        self.opening_browser()
        self.browser.maximize_window()
        self.browser.find_element(By.XPATH, "/html/body/header/div[1]/ul[1]/li[1]/span/span/a").click()
        self.browser.implicitly_wait(5)
        self.browser.find_element(By.ID, "personalaccount-radio").click()
        self.browser.find_element(By.ID, "firstname").send_keys("Thanuja")
        self.browser.find_element(By.ID, "lastname").send_keys("sajja")
        self.browser.find_element(By.ID, "Email").send_keys("sajjathanu@gmail.com")
        self.browser.find_element(By.ID, "password").send_keys("avananya@16")
        self.browser.find_element(By.ID, "EMAIL_REG_FORM_SUBMIT").click()
