import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver')
    request.addfinalizer(wd.quit)
    return wd


def test(driver):
    # goto main page
    driver.get("http://live.guru99.com/index.php/")
    # goto mobilepage
    driver.find_element_by_css_selector(".level0.nav-1.first a").click()
    # read a price of Sony Xperia on products page
    mainprice = driver.find_element_by_css_selector("#product-price-1 > span.price").text
    # goto to Sony Xperia page
    driver.find_element_by_css_selector("#product-collection-image-1").click()
    # read a price of Sony Xperia on its page
    pageprice = driver.find_element_by_css_selector(".price").text
    # assert that prices are same
    assert mainprice == pageprice

