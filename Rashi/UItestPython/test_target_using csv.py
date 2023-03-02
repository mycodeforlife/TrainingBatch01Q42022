from selenium import webdriver
import csv
    # selenium is the name of the file
    # webdriver is the class of the file
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

input_file="test_data.csv"
test_data_map={}

# Function to read csv file and return individual line based on input sent
def data_processor(test_case_id):
    with open(input_file, newline='') as csvfile:

        data= csv.DictReader(csvfile)
        #print(len(list(data)))
        for each_data in data:
            if test_case_id== int(each_data["TestCaseID"]):
                #print(each_data)
                return each_data

@pytest.mark.Smoke
#test case to login and validate information based on test data input in the csv file
def test_case1():
    browser_ff = webdriver.Firefox()  # with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    # First loop to validate the correct site by verifying the Page Title
    for each_case_id  in range (1,2):  #loop
        test_data_input = data_processor(each_case_id)
        print(test_data_input)
        browser_ff.get(test_data_input["URL"])
        page_title = browser_ff.title
        print(page_title)
        expected_title = test_data_input["Expected_Results"]
        assert expected_title in page_title
    #browser_ff.quit()
    # Run all the test cases by reading the csv file one line at a time  and executing each line
    for each_case_id in range(2,20):
        test_data_input = data_processor(each_case_id)
        print(test_data_input)

        # Find the element on the page by XPATH/ID/NAME based on the URL input in CSV
        if test_data_input["URL"]=="XPATH":
            search_web_element = browser_ff.find_element(By.XPATH,test_data_input["Expected_Results"])

        if test_data_input["URL"] == "NAME":
            search_web_element = browser_ff.find_element(By.NAME, "lastnamecreateaccount")

        if test_data_input["URL"] == "ID":
            search_web_element = browser_ff.find_element(By.ID, test_data_input["Expected_Results"])

        #Logic to wait for next page to load
        if test_data_input["URL"]=="WAIT":
            browser_ff.implicitly_wait(test_data_input["Expected_Results"])

        # Logic to perform Action (Click/ Enter Value) based on URL value in CSV
        if test_data_input["URL"] == "ACTION":
            search_web_element.click()

        if test_data_input["URL"] == "ENTER_VALUE":
            search_web_element.send_keys(test_data_input["Expected_Results"] )

        # Logic to validate the findings and perform assert if condition doesnot match
        if test_data_input["URL"] == "VALIDATE":
            error_highlight = search_web_element.text
            assert test_data_input["Expected_Results"] in error_highlight
        #assert search_web_element in search_web_element
