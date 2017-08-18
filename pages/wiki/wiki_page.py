from selenium.webdriver.common.by import By
from base.common import CommonMethods #inherit comonmethods also enables seleniumdriver class
                                      #  as Commonmethods is inherited by it
# adding these 2 imports will indicate in the log output file that the actions were called from login page
import utilities.custom_logger as cl
import logging


class User_registration(CommonMethods):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_content = "searchInput"
    _search_magnifier_icon="searchButton"
    _usermanual_link="Mahara wiki"
    _download_link="Download Mahara"
    _wait_check="sdfskdbkj"

    def enterSearchKeyword(self, keyword):
        self.sendKeys(keyword,self._search_content,"id")

    def clickSearchMagnifier(self):
        self.elementClick(self._search_magnifier_icon,"id")

    def goToMahaWikiPage(self):
        self.elementClick(self._usermanual_link,"link")


    def searchContent(self, keyword):
        self.enterSearchKeyword(keyword)
        self.clickSearchMagnifier()

    def isDownloadLinkPresent(self):
        self.screenShot("Download mahara link check")
        return self.isElementPresent(self._download_link,"link")

    def isTestWaiting(self):
        ele=self.waitForElement(self._download_link,"link",4)

        if ele is not None:
          return True
        else:
          return False




