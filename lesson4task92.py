# coding=utf-8
import pytest
from selenium import webdriver

"""
на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
зайти в каждую из стран и проверить, что зоны расположены в алфавитном порядке
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

    #open "Geo_zones" page
    wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    #creating a list of countries with geozones
    elements = wd.find_elements_by_css_selector(".dataTable .row td:nth-child(3")
    countries = []
    for element in elements:
        countries.append(element.text)

    # creating a list of geozones
    for country in countries:
        wd.find_element_by_link_text(country).click()
        elements = wd.find_elements_by_css_selector(".dataTable tr td:nth-child(3) select option:checked")
        geozones = []
        for element in elements:
            geozones.append(element.text)
        #assert on "зоны расположены в алфавитном порядке"
        sortedgeozones = sorted(geozones)
        assert sortedgeozones == geozones
        wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    print "Test done"




