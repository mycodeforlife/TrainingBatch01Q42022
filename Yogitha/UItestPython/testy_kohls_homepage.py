from selenium import webdriver
import pytest
import csv


input_file = "test_data.csv"
test_data_map = {}


def data_processor(test_case_id):
    with open(input_file, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for each_data in data:
            print(each_data["Test_Case"], test_case_id)
            if test_case_id == int(each_data["Test_Case"]):
                print(each_data)
                return each_data


@pytest.mark.demo
@pytest.mark.sanitytest
def test_case1():
    browser_me = webdriver.Edge()
    for each_case_id in range(1, 3):
        test_data_input = data_processor(each_case_id)
        print(test_data_input)
        browser_me.get(test_data_input["url"])
        page_title = browser_me.title
        #browser_me.find_element(By.link, "")
        print(page_title)
        expected_title = test_data_input["ExpectedValue"]
        assert expected_title in page_title
    browser_me.quit()


@pytest.mark.sanitytest
def test_case2():
    browser_me = webdriver.Edge()
    browser_me.get("https://www.kohls.com")
    page_title = browser_me.title
    print(page_title)
    exepected_title = "Kohl's | Shop Clothing, Shoes, Home, Kitchen, Bedding, Toys & More"
    browser_me.quit()
    assert exepected_title in page_title

