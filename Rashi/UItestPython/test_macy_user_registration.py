from selenium import webdriver
import csv
    # selenium is the name of the file
    # webdriver is the class of the file
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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
    for each_case_id  in range (1,2):
        test_data_input = data_processor(each_case_id)
        print(test_data_input)
        browser_ff.get(test_data_input["URL"])
        page_title = browser_ff.title
        print(page_title)
        expected_title = test_data_input["Expected_Results"]
        assert expected_title in page_title
    browser_ff.quit()


def test_Case2():
    browser_ff = webdriver.Firefox()  # with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    test_data_input = data_processor(1)
    print(test_data_input)
    browser_ff.get(test_data_input["URL"])
    #browser_ff.find_element_by_partial_link_text
    result_element= browser_ff.find_element(By.PARTIAL_LINK_TEXT, 'Sign in')
    #result_element= browser_ff.find_element_by_partial_link_text("drop-down-sign-in")
    #browser_ff.find_element(By.XPATH,'/html/body/header/div/div/div/section[1]/ul/li[3]/div/nav/ul/li/div/div/a/span')

    #search_web_element = browser_ff.find_element(By.ID,"globalSearchInputField")
    #search_web_element.click()
    #search_web_element.send_keys("iphone 14 pro" + Keys.RETURN)
    #xpath_info="//*[@id="drop-down-sign-in"]"
    #result_element= browser_ff.find_element(By.XPATH,xpath_info)
    print (result_element)
    result_element.click()

@pytest.mark.sanitytest
def test_Case3():
    browser_ff = webdriver.Firefox()  # with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    #test_data_input = data_processor(1)
    #print(test_data_input)
    browser_ff.get("https://www.target.com/")
    #browser_ff.find_element_by_partial_link_text
    #result_element= browser_ff.find_element(By.PARTIAL_LINK_TEXT, 'standard-sign-up')
    #result_element= browser_ff.find_element_by_partial_link_text("drop-down-sign-in")
    search_web_element=browser_ff.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/nav/a[4]/div/img')

    #earch_web_element = browser_ff.find_element_by_class_name("styles__ListItemText-sc-diphzn-1 eOhzvD")
    #search_web_element.click()
    #search_web_element.send_keys("iphone 14 pro" + Keys.RETURN)
    #xpath_info="//*[@id="drop-down-sign-in"]"
    #result_element= browser_ff.find_element(By.XPATH,xpath_info)
    #print (result_element)
    search_web_element.click()

    result_element1=browser_ff.find_element_by_id('createAccount')
    result_element1.click()








