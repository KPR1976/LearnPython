import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from guru99parameters import *
import allure


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(driverpath)
    request.addfinalizer(wd.quit)
    return wd

@allure.testcase("case1 - positive")
def test1(driver):
    driver.get(baseurl + "/V4/")
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(login)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("btnLogin").click()
    print driver.find_element_by_css_selector("tr.heading3").get_attribute("textContent")
    #WebDriverWait(driver, 10).until(EC.title_is(condition))
    assert driver.find_element_by_css_selector("tr.heading3").get_attribute("textContent") == "\n    Manger Id : " + login + "\n"

@allure.testcase("case2 - negative")
def test2(driver):
    driver.get(baseurl + "/V4/")
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(wronglogin)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("btnLogin").click()
    alert = driver.switch_to_alert()
    assert alert.text == "User or Password is not valid"

@allure.testcase("case3 - negative")
def test3(driver):
    """

    :type driver: object
    """
    driver.get(baseurl + "/V4/")
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(login)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(wrongpassword)
    driver.find_element_by_name("btnLogin").click()
    #alert = driver.switch_to_alert()
    alert = driver.switch_to_alert()
    assert alert.text == "User or Password is not valid"

@allure.testcase("case4 - negative")
def test4(driver):
    driver.get(baseurl + "/V4/")
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(wronglogin)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(wrongpassword)
    driver.find_element_by_name("btnLogin").click()
    alert = driver.switch_to_alert()
    assert alert.text == "User or Password is not valid"
