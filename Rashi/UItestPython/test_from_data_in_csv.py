from selenium import webdriver
import csv
    # selenium is the name of the file
    # webdriver is the class of the file
import pytest

input_file="test_data.csv"
test_data_map={}

def data_processor(test_case_id):
    with open(input_file, newline='') as csvfile:
        data= csv.DictReader(csvfile)
        for each_data in data:
            if test_case_id== int(each_data["TestCaseID"]):
                #print(each_data)
                return each_data


def test_case1():
    browser_ff = webdriver.Firefox()  # with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    for each_case_id  in range (1,4):
        test_data_input = data_processor(each_case_id)
        print(test_data_input)
        browser_ff.get(test_data_input["URL"])
        page_title = browser_ff.title
        print(page_title)
        expected_title = test_data_input["Expected_Results"]
        assert expected_title in page_title
    browser_ff.quit()




