from selenium.webdriver.common.by import By
from base.common import CommonMethods #inherit comonmethods also enables seleniumdriver class
                                      #  as Commonmethods inherits seleniumwebdriver class
# adding these 2 imports will indicate in the log output file that the actions were called from login page
import utilities.custom_logger as cl
import logging
from configfiles.settings import GlobalVars

class LoginPage(CommonMethods):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _user_name = "login_login_username"
    _password = "login_login_password"
    _login_button = "login_submit"
    _logged_in_as="username"
    _user_manual="Mahara user manual"
    _user_profile="user-icon"

    def enterUname(self, email):
        self.sendKeys(email,self._user_name,"id")

    def enterPassword(self, password):
        self.sendKeys(password,self._password,"id")

    def clickLoginButton(self):
        self.elementClick(self._login_button,"id")

    def login(self):
        self.enterUname(GlobalVars().fetchVar("userName"))
        self.enterPassword(GlobalVars().fetchVar("password"))
        self.clickLoginButton()
        self.screenShot(self.__module__.title())

    def verifyLogin(self):
        assert self.isElementPresent(self._logged_in_as,"class")
        assert self.getElement(self._logged_in_as,"class").get_attribute("text")=="James Jetts"

    def accessProfile(self):
        self.getElement(self._user_profile,"class").click()

    def verifyLoginTitle(self,expectedTitle):
        assert self.verifyPageTitle(expectedTitle)



