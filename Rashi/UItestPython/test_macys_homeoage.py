from selenium import webdriver
    # selenium is the name of the file
    # webdriver is the class of the file
import pytest
import csv


input_file = "test_data.csv"
test_data_map={}


def data_processor(test_case_id):
    with open(input_file,newline='')as csvfile:
        data=csv.DictReader(csvfile)
        for each_data in data:
            print(each_data["test_case"]),test_case_id
            if test_case_id==each_data["test_case"]:
                 # print each_data
                return each_data



@pytest.mark.demo

def test_case1():
    browser_ff = webdriver.Firefox()  #with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    browser_ff.get("https://www.amazon.com")
    page_title = browser_ff.title
    print(page_title)
    expected_title = "Ebay"
    browser_ff.quit()
    assert expected_title == page_title


@pytest.mark.sanitytest
def test_case2():
    browser_ff = webdriver.Firefox()  # with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    browser_ff.get("https://www.macys.com")
    page_title = browser_ff.title
    print(page_title)
    expected_title = "macys"
    browser_ff.quit()
    assert expected_title in page_title
