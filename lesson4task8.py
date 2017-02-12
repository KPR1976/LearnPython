import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def wd(request):
    wd = webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver')
    #wd = webdriver.Firefox(executable_path='/Users/KPR/Mystuff/SeleniumDrivers/geckodriver')
    request.addfinalizer(wd.quit)
    return wd


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0

def test(wd):
    wd.get("http://localhost/litecart/")
    pageelements = wd.find_elements_by_css_selector(".product")
    print len(pageelements)
    for i in range (len(pageelements)):
        assert len(pageelements[i].find_elements_by_css_selector(".sticker")) == 1


