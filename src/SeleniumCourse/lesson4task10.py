# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""
Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара в учебном приложении litecart.

Более точно, нужно открыть главную страницу, выбрать первый товар в категории Campaigns и проверить следующее:

а) на главной странице и на странице товара совпадает текст названия товара
б) на главной странице и на странице товара совпадают цены (обычная и акционная)
в) обычная цена серая и зачёркнутая, а акционная цена красная и жирная (это надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
г) акционная цена крупнее, чем обычная (это надо проверить на каждой странице независимо)
"""

@pytest.fixture
def wd(request):
    wd = webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver')
    request.addfinalizer(wd.quit)
    return wd

def test(wd):
    #open mainpage of shop
    wd.get("http://localhost/litecart/")
    # get an attributes from main page
    nameonpage = wd.find_element_by_css_selector("#box-campaigns .product .name").get_attribute("textContent")
    mainpage = wd.find_element_by_css_selector("#box-campaigns .price-wrapper")
    regularprice = mainpage.find_element_by_css_selector(".regular-price").get_attribute("textContent")
    regularpricecolor = mainpage.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    regularpricedec = mainpage.find_element_by_css_selector(".regular-price").tag_name
    regulapricefontsize = mainpage.find_element_by_css_selector(".regular-price").value_of_css_property("font-size").replace("px","")
    campaignprice = mainpage.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
    campaignpricecolor = mainpage.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    campaignpricedec = mainpage.find_element_by_css_selector(".campaign-price").tag_name
    campaignpricefontsize = mainpage.find_element_by_css_selector(".campaign-price").value_of_css_property(
        "font-size").replace("px", "")

    # go to product page
    wd.find_element_by_css_selector("#box-campaigns .link").click()
    # get an attributes from product page
    nameonpagep = wd.find_element_by_css_selector("#box-product .title").get_attribute("textContent")
    mainpage = wd.find_element_by_css_selector("#box-product .price-wrapper")
    regularpricep = mainpage.find_element_by_css_selector(".regular-price").get_attribute("textContent")
    regularpricecolorp = mainpage.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    regularpricedecp = mainpage.find_element_by_css_selector(".regular-price").tag_name
    regulapricefontsizep = mainpage.find_element_by_css_selector(".regular-price").value_of_css_property(
        "font-size").replace("px", "")
    campaignpricep = mainpage.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
    campaignpricecolorp = mainpage.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    campaignpricedecp = mainpage.find_element_by_css_selector(".campaign-price").tag_name
    campaignpricefontsizep = mainpage.find_element_by_css_selector(".campaign-price").value_of_css_property(
        "font-size").replace("px", "")

    #assert on а) на главной странице и на странице товара совпадает текст названия товара
    assert nameonpage == nameonpagep
    #assert on б) на главной странице и на странице товара совпадают цены (обычная и акционная)
    assert regularprice == regularpricep
    assert campaignprice == campaignpricep
    # assert on в) обычная цена серая и зачёркнутая, а акционная цена красная и жирная
    #mainpage
    assert regularpricecolor == "rgba(119, 119, 119, 1)"
    assert regularpricedec == "s"
    assert campaignpricecolor == "rgba(204, 0, 0, 1)"
    assert campaignpricedec == "strong"
    #productpage
    assert regularpricecolorp == "rgba(102, 102, 102, 1)"
    assert regularpricedecp == "s"
    assert campaignpricecolorp == "rgba(204, 0, 0, 1)"
    assert campaignpricedecp == "strong"
    #assert on г) акционная цена крупнее, чем обычная
    assert float(regulapricefontsize) < float(campaignpricefontsize)
    assert float(regulapricefontsizep) < float(campaignpricefontsizep)



