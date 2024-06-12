import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser=="edge":
        driver=webdriver.Edge()

    elif browser=="firefox":
        driver=webdriver.Firefox()

    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):    # this will get the value from the terminal/command line --it is called hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will resturn the browser value to the setup method
    return request.config.getoption("--browser")


########  To generate the pytest html reports , need to add below hooks #######

## these/below are the pre defined hooks which are already defined in the pytest document

