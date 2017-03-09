import pytest
from selenium import webdriver
from guru99parameters import *


@pytest.fixture
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("forceDevToolsScreenshot", True)
    chrome_options.add_argument("--kiosk")
    wd = webdriver.Chrome(driverpath, chrome_options=chrome_options)
    #wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd


def test(driver):
    driver.get(baseurl + "/V4/")
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(login)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("btnLogin").click()
    print driver.find_element_by_css_selector("tr.heading3").get_attribute("textContent")
    # WebDriverWait(driver, 10).until(EC.title_is(condition))
    assert driver.find_element_by_css_selector("tr.heading3").get_attribute(
        "textContent") == "\n    Manger Id : " + login + "\n"
    driver.get_screenshot_as_file('screen.png')


"""
def test2(driver):
    driver.get(baseurl + "/V4/")
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(wronglogin)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("btnLogin").click()
    alert = driver.switch_to_alert()
    assert alert.text == "User or Password is not valid"

def test3(driver):
    driver.get(baseurl + "/V4/")
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(login)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(wrongpassword)
    driver.find_element_by_name("btnLogin").click()
    alert = driver.switch_to_alert()
    assert alert.text == "User or Password is not valid"

def test4(driver):
    driver.get(baseurl + "/V4/")
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(wronglogin)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(wrongpassword)
    driver.find_element_by_name("btnLogin").click()
    alert = driver.switch_to_alert()
    assert alert.text == "User or Password is not valid"
"""
