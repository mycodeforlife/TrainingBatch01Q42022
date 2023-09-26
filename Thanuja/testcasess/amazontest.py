from datetime import datetime

from selenium import webdriver
import pytest
import csv
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
input_test_file = "test.csv"


def read_input(testcase_id):
    with(open(input_test_file, newline='')) as csvfile:
        reader = csv.DictReader(csvfile)
        for each in reader:
            if testcase_id == int(each["TestCaseID"]):
                return each


class TestClass:

    MaxTimeOut = 30
    browser_open = webdriver.Firefox()

    @pytest.mark.demo1
    def test_case1(self):
        testcase_id = read_input(1)
        self.browser_open.get(testcase_id["URL"])
        browser_title = self.browser_open.title
        print(browser_title)
        title = testcase_id["Expected_Results"]
        assert title in browser_title

    @pytest.mark.demo
    def test_case2(self):
        self.browser_open.get("https://amazon.com")
        # time.sleep(10)  # implicit wait
        # web_element = browser_open.find_element(By.ID, "twotabsearchtextbox")
        print(datetime.now())
        EC = expected_conditions
        try:
            web_element = WebDriverWait(self.browser_open, self.MaxTimeOut).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        except:
            print("Not abel to locate element")
        else:
            web_element.send_keys("monopoly cards" + Keys.ENTER)
        print(datetime.now())

