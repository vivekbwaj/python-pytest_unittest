from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.utils import utils

class CommonMethods(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits CommonMethods class

        Returns:
            None
        """
        super(CommonMethods, self).__init__(driver)
        self.driver = driver
        self.utils = utils()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.utils.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False