import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    #caps = DesiredCapabilities.FIREFOX
    wd = webdriver.Firefox(executable_path='/Users/KPR/Mystuff/SeleniumDrivers/geckodriver')
    print (wd.capabilities)
    request.addfinalizer(wd.quit)

    return wd

def test_example(driver):
    driver.get("http://www.google.com/ncr")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Google Search"))