import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver')
    request.addfinalizer(wd.quit)
    return wd


def test(driver):
    # goto main page
    driver.get("http://live.guru99.com/index.php/")
    # assert text on page
    assert (driver.find_element_by_css_selector("h2").text) \
        == 'THIS IS DEMO SITE FOR   '
    # goto mobile page
    driver.find_element_by_css_selector(".level0.nav-1.first a").click()
    # assert on page title
    assert (driver.find_element_by_css_selector("title").get_attribute("textContent")) \
        == 'Mobile'
    # select products by name
    dropdown = Select(driver.find_element_by_css_selector(".sort-by select"))
    dropdown.select_by_visible_text("Name")
    products = driver.find_elements_by_css_selector(".item")
    productssorted = sorted(products)
    # assert sorting
    assert products == productssorted
