import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


@pytest.mark.regression
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/Login.xlsx"
    logger = LogGen.loggen()

    def test_login_DDT(self,setup):
        self.logger.info("**********Test_002_Login_DDT************")
        self.logger.info("***************Login test**************")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowscount(self.path,'Sheet1')
        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.pwd=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            lst_status=[]  # emptylist variable
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************Login Passed ***************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.exp == "Fail":
                    self.logger.error("########Login failed#####")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.error("###############Login Failed #####################")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("******Login Passed********")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test Passed...................")
            self.driver.close()
            assert True
        else:
            self.logger.error("#####Login DDT failed #######")
            self.driver.close()
            assert False

        self.logger.info("****DDT is finished***********")

