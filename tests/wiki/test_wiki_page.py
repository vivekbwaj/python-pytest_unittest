from pages.wiki.wiki_page import User_registration
import pytest,unittest

@pytest.mark.usefixtures("configSetUp","setUp")
class Test_WikiPageCases(unittest.TestCase): #the class name should be appended by Test in order to be recognized by pytest

    @pytest.fixture(autouse=True) # Autouse makes the loginSetUp method available to all other test methods in this class
    def wikiPageSetUp(self,configSetUp):
        self.reg = User_registration(self.driver)

    def test_SearchContent(self):
        self.reg.goToMahaWikiPage()
        self.reg.searchContent("download")
        assert self.reg.isDownloadLinkPresent()
        # assert self.reg.isTestWaiting()



        # E:\Python-SeleniumFramework\PythonFramework>py.test -v -s tests/home/login_tests.py
# this will generate log file in root directory