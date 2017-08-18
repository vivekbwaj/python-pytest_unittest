import unittest
from tests.home.login_tests import Test_LoginCases
from tests.wiki.test_wiki_page import Test_WikiPageCases

lgnTests=unittest.TestLoader().loadTestsFromTestCase(Test_LoginCases)
wikiTests=unittest.TestLoader().loadTestsFromTestCase(Test_WikiPageCases)

smoke=unittest.TestSuite([lgnTests])
smoke2=unittest.TestSuite([wikiTests])

unittest.TextTestRunner(verbosity=1).run(smoke)
unittest.TextTestRunner(verbosity=1).run(smoke2)
