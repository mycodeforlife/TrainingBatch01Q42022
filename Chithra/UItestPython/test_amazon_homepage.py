from selenium import webdriver
import pytest

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


