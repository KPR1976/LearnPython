import pytest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver')
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.google.com/ncr")
    driver.find_element_by_name("q").send_keys("webdriver")
    btnG = driver.find_element_by_name("btnG")
    btnG.click()
    WebDriverWait(driver, 30).until(EC.title_is("webdriver - Google Search"))