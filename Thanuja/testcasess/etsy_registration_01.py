from selenium import webdriver
import csv
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

input_test_file = "test2.csv"


def read_input(testcase_id):
    with(open(input_test_file, 'r', newline='')) as csvfile:
        reader = csv.DictReader(csvfile)
        for each in reader:
            if testcase_id == int(each["TestCaseID"]):
                print("hello")
                print(testcase_id,each["TestCaseID"])
                return each
            else:
                print("else")
                print(testcase_id, each["TestCaseID"])


class TestCaseAutomation:

    input_file = read_input(1)

    @pytest.fixture(autouse=True)
    def opening_browser(self):
        self.input_file = read_input(1)

    # checking the title name is correct
    @pytest.mark.demo
    def test_url_page(self):
        self.input_file = read_input(1)
        print(self.input_file["URL"])
        browser = webdriver.Firefox()
        browser.get(self.input_file["URL"])
        browser.maximize_window()
        browser.implicitly_wait(5)
        get_title = self.browser.title
        print(get_title)
        browser.get(self.input_file["Expected_Results"])
        browser.quit()

    def etsy_registration(self):
        self.opening_browser()
        self.browser.maximize_window()
        self.browser.find_element(By.XPATH, "/html/body/div[2]/header/div[4]/nav/ul/li[1]/button").click()
        self.browser.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div[3]"
                                            "/div/div/div/div/div/div[2]/form/div[1]/div/div[1]/div/button").click()
        self.browser.find_element(By.NAME, "email").send_keys("sajjathanuja+@gmail.com")
        self.browser.find_element(By.NAME, "first_name").send_keys("thanuja")
        self.browser.find_element(By.NAME, "password").send_keys("avananya@16")
        self.browser.find_element(By.NAME, "submit_attempt").click()

    def etsy_search_for_item(self):
        self.opening_browser()
        self.browser.maximize_window()
        search_bar = self.browser.find_element(By.NAME, "search_query")
        self.browser.implicitly_wait(10)
        search_bar.send_keys("sofa", + Keys.ENTER)
