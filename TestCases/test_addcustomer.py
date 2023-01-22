import random
import string
import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType


@pytest.mark.sanity
@allure.severity(allure.severity_level.CRITICAL)
class Test_003_Addcustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_addcustomer(self,setup):
        self.logger.info("****** Starting Test_003_Add Customer***************")
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
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error("###############Login Failed #####################")
            assert False

        self.ac=AddCustomer(setup)
        self.logger.info("****** Clicking on Customermenu/submenu ***************")
        self.ac.clickCustomer()
        time.sleep(2)
        self.ac.clickAddnew()
        self.logger.info("************* Adding Customer details**************")
        self.email=random_generator()+"@gmail.com"
        self.ac.setEmail(self.email)
        time.sleep(3)
        self.ac.setPassword("Test1234")
        self.ac.setFname("Lewis")
        self.ac.setLname("Henry")
        self.ac.setDOB("11/10/1989")
        self.ac.setGender("Male")
        self.ac.setCompanyname("Amazon labs")
        self.logger.info("Selecting customer role")
        self.ac.setCustomerRoles("Guests")
        self.logger.info("Selected a guests role")
        self.ac.setManagerofVendor("Vendor 1")
        self.ac.setAdminContent("This is for testing")
        self.ac.clickOnSave()
        time.sleep(4)
        self.logger.info("*********** Added Customer Details************")
        self.act_title = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]").text
        print(self.act_title)
        if 'The new customer has been added successfully.' not in self.act_title:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer.png")
            self.logger.info("########## Test case Add Customer Failed #############")
            assert False
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test add customer ",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("********** Test case Add Customer Passed**************")
            assert True

        self.driver.close()
        self.logger.info("*********Ending Add Customer Test ********")


# This method generates and returns a random email
def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))