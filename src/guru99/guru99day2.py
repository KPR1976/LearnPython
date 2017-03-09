import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from guru99parameters import *


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(driverpath)
    request.addfinalizer(wd.quit)
    return wd


def test(driver):
    driver.get(baseurl + "/V4/")
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(login)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("btnLogin").click()
    WebDriverWait(driver, 10).until(EC.title_is(condition))


