import pytest
from selenium import webdriver

"""
на странице http://localhost/litecart/admin/?app=countries&doc=countries
а) проверить, что страны расположены в алфавитном порядке
б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить, что зоны расположены в алфавитном порядке
"""

@pytest.fixture
def wd(request):
    wd = webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver')
    request.addfinalizer(wd.quit)
    return wd

def test(wd):
    # open adminpage
    wd.get("http://localhost/litecart/admin")
    wd.find_element_by_name("username").send_keys("admin")
    wd.find_element_by_name("password").send_keys("admin")
    wd.find_element_by_name("login").click()

    #open "Countries" page
    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    #creating a list of countries and countries with timezones from datatable
    elements = wd.find_elements_by_css_selector(".dataTable .row")
    countries = []
    countrieswithzones = []
    for element in elements:
        country = element.find_element_by_css_selector("td:nth-child(5) a")
        countries.append(country.text)
        countrywithzone = element.find_element_by_css_selector("td:nth-child(6)")
        if countrywithzone.text != "0":
            countrieswithzones.append(country.text)

    # assert on "проверить, что страны расположены в алфавитном порядке"
    countriessorted = sorted(countries)
    assert countries == countriessorted
    print "Test A done"

    # creating a list of timezonesnames
    for countrywithzone in countrieswithzones:
        wd.find_element_by_link_text(countrywithzone).click()
        elements = wd.find_elements_by_css_selector(".dataTable tr td:nth-child(3)")
        zones = []
        for element in elements:
            if element.get_attribute("textContent") != "":
                zones.append(element.get_attribute("textContent"))
        # assert on "для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить, что зоны расположены в алфавитном порядке"
        zonessorted = sorted(zones)
        assert zones == zonessorted
        wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    print "Test B done"





