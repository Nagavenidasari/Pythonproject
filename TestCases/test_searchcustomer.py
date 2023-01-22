import time
import pytest
import allure
from allure_commons.types import AttachmentType

from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_004_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_searchCustomerByEmail(self,setup):
        self.driver = setup
        self.logger.info("*********** Starting Test_004 Search Customer by Email*******")
        setup.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*************Login Passed ***************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error("###############Login Failed #####################")
            assert False
        self.ac=AddCustomer(setup)
        self.logger.info("******** clicking on customers menu and submenu ********")
        self.ac.clickCustomer()
        self.sc=SearchCustomer(setup)
        self.logger.info("********* Searching customer by Email *********")
        self.sc.setEmail("victoria_victoria@nopCommerce.com")
        time.sleep(2)
        self.sc.clickSearch()
        time.sleep(5)
        status = self.sc.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        if status == True:
            self.logger.info("*********** Test Search customer by Email Passed *************")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test search customer by email",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchcustbyEmail.png")
            self.logger.error("##### Test Search customer by Email Failed ############")
            assert False
        self.driver.close()


    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_searchCustomerByName(self,setup):
        self.driver = setup
        self.logger.info("*********** Starting Test_004 Search Customer ny Name*******")
        setup.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*************Login Passed ***************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error("###############Login Failed #####################")
            assert False
        self.ac=AddCustomer(setup)
        self.logger.info("******** clicking on customers menu and submenu ********")
        self.ac.clickCustomer()
        self.sc=SearchCustomer(setup)
        self.logger.info("********* Searching customer by Name *********")
        self.sc.setFirstname("Victoria")
        self.sc.setLastname("Terces")
        time.sleep(2)
        self.sc.clickSearch()
        time.sleep(5)
        status1 = self.sc.searchCustomerByName("Nagaveni")
        if status1 == True:
            self.logger.info("*********** Test Search customer by Name Passed *************")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test search customer by name",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchcustbyName.png")
            self.logger.error("##### Test Search customer by Name Failed ############")
            assert False
        self.driver.close()
