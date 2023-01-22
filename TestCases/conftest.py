import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Launching Chrome Browser .......")
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.implicitly_wait(20)
    elif browser == 'firefox':
        print("Launching Firefox browser......")
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities["marionette"] = False
        driver = webdriver.Firefox(executable_path='C:\seleniumdrivers\geckodriver.exe', capabilities=capabilities)
        driver.maximize_window()
        driver.implicitly_wait(20)
    else:
        print("Launching Edge browser......")
        driver=webdriver.Edge(executable_path='C:\\Drivers\\msedgedriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(20)
    return driver

def pytest_addoption(parser): # this will get the value from CLI hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will resturn the browser value to setup method
    return request.config.getoption("--browser")


#### to generate PyTest HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Nagaveni Tester'

# Hook to delete/Modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)