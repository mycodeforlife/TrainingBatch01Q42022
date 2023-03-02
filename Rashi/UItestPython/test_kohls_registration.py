from selenium import webdriver
import csv
    # selenium is the name of the file
    # webdriver is the class of the file
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.Element_verf

def test_Case3():
   browser_ff = webdriver.Firefox()
   browser_ff.get ("https://www.target.com/")   # open target web page
   print(browser_ff.title)  # print title of the page

   # browser_ff.find_element_by_partial_link_text
   # result_element= browser_ff.find_element(By.PARTIAL_LINK_TEXT, 'standard-sign-up')
   # result_element= browser_ff.find_element_by_partial_link_text("drop-down-sign-in")
   search_web_element = browser_ff.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/nav/a[4]/div/img')  # Find element for SIGN _IN

   # earch_web_element = browser_ff.find_element_by_class_name("styles__ListItemText-sc-diphzn-1 eOhzvD")
   # search_web_element.click()
   # search_web_element.send_keys("iphone 14 pro" + Keys.RETURN)
   # xpath_info="//*[@id="drop-down-sign-in"]"
   # result_element= browser_ff.find_element(By.XPATH,xpath_info)
   # print (result_element)
   search_web_element.click()  # Click on Sign IN

   search_web_element = browser_ff.find_element(By.XPATH,'/html/body/div[9]/div/div/div[2]/ul/li[2]/a/span')  #Find Element for Create Account
   search_web_element.click()  # Click on Create Account
   browser_ff.implicitly_wait(10)  # Wait for page to load
   search_web_element = browser_ff.find_element(By.ID,'lastname')   # find element for last name
   search_web_element.send_keys("iphone 14 pro" + Keys.RETURN)  # Enter value in the last name field and click enter
   search_web_element = browser_ff.find_element(By.ID,'username--ErrorMessage')  # find element for the warning message (Email)
   expected_result = "Please enter your email" # set the expected value
   current_value = search_web_element.text  # Save the current value on the page
   assert expected_result in current_value  # assert in case of values donot match

    #result_element = browser_ff.find_element(By.XPATH, '//*[@id="listaccountNav-createAccount"]/a')
    #result_element.click()
    #print(browser_ff.title)
    #newURl = browser_ff.window_handles[0]
    #browser_ff.switch_to.window(newURl)
    #browser_ff.implicitly_wait(10)  # seconds
    #element = browser_ff.find_element(By.NAME,"lastnamecreateaccount")
    #element.send_keys("iphone 14 pro" + Keys.RETURN)

    #element1= browser_ff.find_element(By.ID,"username--ErrorMessage")
    #error_highlight= element1.text
    #print(error_highlight)
    #new_page= browser_ff.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/div[2]/form/button/span")
    #element.click()
    #new_page.send_keys("iphone 14 pro" + Keys.RETURN)

    #search_web_element=browser_ff.find_element_by_class_name( "utility-item-link account utility-nav-wallet-svg")
    #search_web_element.click()
    #search_web_element1 = browser_ff.find_element(By.CLASS,'createaccount_landingpage rd-signInBtn textWhite rd-btnGreen mT20 kas-loginPage-createAccount-button-createAccountClick')
    #search_web_element1.click()
    #browser_ff.find_element_by_partial_link_text
    #result_element= browser_ff.find_element(By.PARTIAL_LINK_TEXT, 'standard-sign-up')
    #result_element= browser_ff.find_element_by_partial_link_text("drop-down-sign-in")
    #search_web_element=browser_ff.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/nav/a[4]/div/img')

    #earch_web_element = browser_ff.find_element_by_class_name("styles__ListItemText-sc-diphzn-1 eOhzvD")
    #search_web_element.click()
    #search_web_element.send_keys("iphone 14 pro" + Keys.RETURN)
    #xpath_info="//*[@id="drop-down-sign-in"]"
    #result_element= browser_ff.find_element(By.XPATH,xpath_info)
    #print (result_element)

    #result_element=browser_ff.find_element(By.XPATH,'/html/body/div[9]/div/div/div[2]/ul/li[2]/a/span')
    #result_element.click()
    #result_element1=browser_ff.find_element_by_id('createAccount')
    #result_element1.click()


