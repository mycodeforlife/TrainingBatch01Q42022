from selenium import webdriver
    # selenium is the name of the file
    # webdriver is the class of the file

import pytest
def test_Case1():
    browser_ff = webdriver.Firefox()  #with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    browser_ff.get("https://www.amazon.com")
    page_title = browser_ff.title
    print(page_title)
    expected_title = "Ebay"
    browser_ff.quit()
    assert expected_title ==page_title

def test_Case2():
    browser_ff = webdriver.Firefox()  # with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    browser_ff.get("https://www.amazon.com")
    page_title = browser_ff.title
    print(page_title)
    expected_title = "Amazon"
    browser_ff.quit()
    assert expected_title in  page_title

@pytest.mark.case3
def test_Case3():
    browser_ff = webdriver.Firefox()  # with brackets means we are calling a function (Ff) and without brackets means we are calling a variables (ff)
    browser_ff.get("https://www.amazon.com")
    page_title = browser_ff.title
    print(page_title)
    expected_title = "Amazon"
    browser_ff.quit()
    assert expected_title in  page_title