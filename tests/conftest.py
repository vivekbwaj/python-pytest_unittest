import pytest
from selenium import webdriver
from base.webdriverSetup import WebdriverSetup

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.fixture(scope="class")
def configSetUp(request, browser):
    wds=WebdriverSetup(browser)
    driver=wds.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Shutting down browser")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
