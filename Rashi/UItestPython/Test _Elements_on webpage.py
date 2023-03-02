from selenium import webdriver
    # selenium is the name of the file
    # webdriver is the class of the file

import pytest
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.by import By


@pytest.mark.case3
def test_Case1():
    browser_ff = webdriver.Firefox()  # with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    browser_ff.get("https://www.amazon.com")
    page_title = browser_ff.title
    print(page_title)
    expected_title = "Amazon"
    browser_ff.quit()
    assert expected_title in  page_title

@pytest.mark.test2
def test_Case2():
    browser_ff = webdriver.Firefox()  # with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    browser_ff.get("https://www.amazon.com")

    search_web_element = browser_ff.find_element(By.ID,"twotabsearchtextbox")
    search_web_element.send_keys("iphone 14 pro" + Keys.RETURN)
    xpath_info="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span"
    result_element= browser_ff.find_element(By.XPATH,xpath_info)
    print (result_element)



