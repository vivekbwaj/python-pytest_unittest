from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import pytest,unittest

@pytest.mark.usefixtures("configSetUp","setUp")
class Test_LoginCases(unittest.TestCase): #the class name should be appended by Test in order to be recognized
                                              # by pytest
    @pytest.fixture(autouse=True) # Autouse makes the loginSetUp method available to all other test methods
                                                      #  in this class
    def loginSetUp(self,configSetUp):
        self.lp = LoginPage(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login()
        self.lp.login                               #self.lp is available because of autouse keyword above
        print("The title of the page is "+self.driver.title)
        self.lp.verifyLogin()

    @pytest.mark.run(order=3)
    def test_goToProfile(self):
        self.lp.accessProfile()

    @pytest.mark.run(order=1)
    def test_TitleCheck(self):
        self.lp.verifyLoginTitle("mahara")



        # E:\Python-SeleniumFramework\PythonFramework>py.test -v -s tests/home/login_tests.py
# this will generate log file in root directory