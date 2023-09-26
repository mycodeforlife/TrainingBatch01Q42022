from selenium import webdriver
import pytest
import csv

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

input_test_data_file = "testdata.csv"


def read_input_data():
    pass


def test_Case1():
    browser_ff = webdriver.Firefox()
    browser_ff.get("https://www.amazon.com")
    page_title = browser_ff.title
    print(page_title)
    exepected_title = "Ebay"
    browser_ff.quit()
    assert exepected_title == page_title


@pytest.mark.smoke
def test_Case2():
    browser_ff = webdriver.Firefox()
    browser_ff.get("https://www.amazon.com")
    page_title = browser_ff.title
    print(page_title)
    exepected_title = "Amazon.com"
    browser_ff.quit()
    assert exepected_title in page_title




# //*[@id="nav-link-accountList-nav-line-1"]

@pytest.mark.test4
def test_case4():
    browser_ff = webdriver.Firefox()
    browser_ff.get("https://www.amazon.com")
    search_web_element = browser_ff.find_element(By.ID, "twotabsearchtextbox")
    search_web_element.send_keys("iPhone 14 Pro" + Keys.ENTER)
    x_path_info = "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span"
    result_element = browser_ff.find_element(By.XPATH,x_path_info)
    print(result_element)







'''
HTML :  Hyper Text Markup Language 
CSS: Style Sheets 
JavaScript: does logical part of the code in Webpage. 

'''
