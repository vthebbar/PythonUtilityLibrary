# Pytest fixtures and reusable codes for launching browser

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Fixture method To launch browsers

@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
    elif browser == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
        driver.maximize_window()
    else:
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver.maximize_window()

    return driver


# To read browser name from command line argument provided in terminal or cmd

def pytest_addoption(parser):
    parser.addoption("--browser")


#  Fixture method to pass browser name to setup method

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
