#import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = False
driver = webdriver.Firefox(executable_path='C:\seleniumdrivers\geckodriver.exe', capabilities=capabilities)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.google.com")


# ChromeOptions class to add chrome browser options

chrome_options = webdriver.ChromeOptions()

# add option to open maximized browser with add_argument method

chrome_options.add_argument("--start-maximized")

# add option to open browser headless mode with add_argument method

chrome_options.add_argument("headless")

# add option to accept browser certificate errors with add_argument

chrome_options.add_argument("--ignore-certificate-errors")

# chrome browser invocation with options parameter

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe",

options = chrome_options)

# launch a URL in browser

driver.get("https://rahulshettyacademy.com/angularpractice/")

