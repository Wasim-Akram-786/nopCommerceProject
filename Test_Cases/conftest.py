import random
import string

import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome(executable_path='.\\Driver\\chromedriver.exe')
    elif browser == 'Firefox':
        driver=webdriver.Firefox()
    return driver


def pytest_addoption(parser):

    return parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return  request.config.getoption("--browser")

#----------------Pytest HTML Reports -------------------------------

# it is hooks for adding enviroment info to the report

def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester Name'] = 'Wasim'


@pytest.mark.optionalhook
def Pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop('Plugins',None)



