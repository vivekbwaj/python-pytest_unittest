import traceback
from selenium import webdriver
from configfiles.settings import GlobalVars

class WebdriverSetup():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):

        baseURL=GlobalVars().fetchVar("websiteURL")
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.PhantomJS()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Loading browser with App URL
        driver.get(baseURL)
        return driver