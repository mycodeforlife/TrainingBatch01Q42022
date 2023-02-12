from selenium import webdriver
import pytest


def test_case1():
    browser_me = webdriver.Edge()
    browser_me.get("https://www.kohls.com")
    page_title = browser_me.title
    print(page_title)
    exepected_title = "Ebay"
    browser_me.quit()
    assert exepected_title in page_title


def test_case2():
    browser_me = webdriver.Edge()
    browser_me.get("https://www.kohls.com")
    page_title = browser_me.title
    print(page_title)
    exepected_title = "Kohl's | Shop Clothing, Shoes, Home, Kitchen, Bedding, Toys & More"
    browser_me.quit()
    assert exepected_title in page_title

