import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "found")
    def on_exception(self, exception, driver):
        #driver.get_screenshot_as_file('errorscreennew.png')
        #driver.save_screenshot('error.png')
        print(exception)

@pytest.fixture
def wd(request):
    #wd = webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("forceDevToolsScreenshot",True)
    #print chrome_options.experim
    wd = EventFiringWebDriver(webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver',chrome_options=chrome_options), MyListener())
    #wd = EventFiringWebDriver(webdriver.Chrome('/Users/KPR/Mystuff/SeleniumDrivers/chromedriver'), MyListener())
    request.addfinalizer(wd.quit)
    return wd


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0

def test(wd):
    wd.get("http://localhost/litecart/admin")
    wd.find_element_by_name("username").send_keys("admin")
    wd.find_element_by_name("password").send_keys("admin")
    wd.find_element_by_name("login").click()
    #wd.get_screenshot_as_file('mainpage.png')
    pageelements= wd.find_elements_by_css_selector("li#app- a")
    for i in xrange (len(pageelements)):
        link = wd.find_elements_by_css_selector("li#app-")
        link[i].click()
        assert len(wd.find_elements_by_tag_name('h1')) == 1
        childelements = wd.find_elements_by_css_selector("li[id^=doc]")
        if len(childelements) > 0:
            for j in range(len(childelements)):
                clink = wd.find_elements_by_css_selector("li[id^=doc] a")
                clink[j].click()
                assert len(wd.find_elements_by_tag_name('h1')) == 1
    #wd.quit()

