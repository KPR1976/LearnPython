import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver')
    request.addfinalizer(wd.quit)
    return wd


def test(driver):
    driver.get("http://www.demo.guru99.com/V4/")
    driver.find_element_by_name("uid").send_keys("mngr68231")
    driver.find_element_by_name("password").send_keys("bebAsar")
    driver.find_element_by_name("btnLogin").click()
    WebDriverWait(driver, 10).until(EC.title_is("Guru99 Bank Manager HomePage"))