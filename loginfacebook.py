import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):

    wd = webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver')
    wd.page_source
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.facebook.com");
    driver.find_element_by_name("email").send_keys("jforkpr+facebook@gmail.com");
    driver.find_element_by_name("pass").send_keys("!qaz@wsx");
    driver.find_element_by_id("loginbutton").click();
    #WebDriverWait(driver,10).until(EC.presence_of_element_located(driver.find_element_by_name('Profile'))) ;