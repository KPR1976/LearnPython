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
    # add to cart 1 Xperia
    driver.find_element_by_xpath(".//button[contains(@onclick, '/product/1')]").click()
    # update quantity in cart from 1 to 1000
    driver.find_element_by_css_selector(".product-cart-actions .input-text.qty").clear()
    driver.find_element_by_css_selector(".product-cart-actions .input-text.qty").send_keys('1000')
    driver.find_element_by_css_selector(".button.btn-update[name='update_cart_action']").click()
    # assert on error message
    assert driver.find_element_by_css_selector(".error-msg").text == \
        "Some of the products cannot be ordered in requested quantity."
    # emptying cart
    driver.find_element_by_css_selector("#empty_cart_button").click()
    # assert that cart is empty
    assert driver.find_element_by_tag_name("h1").text == \
        "SHOPPING CART IS EMPTY"

