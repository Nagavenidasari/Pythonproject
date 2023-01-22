import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from allure_commons.types import AttachmentType

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_homePageTitle(self,setup):
        self.logger.info("**********Test_001_Login************")
        self.logger.info("***************Verifying HomePage Title**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************Verify Homepage Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("###############Verify Homepage Failed #####################")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self,setup):
        self.logger.info("**********Test_001_Login************")
        self.logger.info("***************Login test**************")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*************Login Passed ***************")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test Login",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error("###############Login Failed #####################")
            assert False

        self.lp.clickLogout()
        self.driver.close()








