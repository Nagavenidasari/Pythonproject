import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AddCustomer:
    lnkCustomers_menu_xpath="//a[@href='#' ]//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[@class='btn btn-primary']"
    txtEmail_id="Email"
    txtPassword_id="Password"
    textFirstname_id="FirstName"
    textLastname_id="LastName"
    rdbtnMaleGender_id="Gender_Male"
    rdbtnFemaleGender_id="Gender_Female"
    txtDob_xpath="//*[@id='DateOfBirth']"
    txtCompanyName_id="Company"
    txtCustomerroles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    lstitemForummoderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    drpManagerofVendor_xpath="//*[@id='VendorId']"
    txtAdmincomment_xpath="//*[@id='AdminComment']"
    btnSave_name="save"




    def __init__(self,driver):
        self.driver = driver
    def clickCustomer(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()
    def clickAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()
    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)
    def setPassword(self,pwd):
        self.driver.find_element(By.ID,self.txtPassword_id).send_keys(pwd)
    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)
    def setFname(self,fname):
        self.driver.find_element(By.ID,self.textFirstname_id).send_keys(fname)
    def setLname(self,lname):
        self.driver.find_element(By.ID,self.textLastname_id).send_keys(lname)
    def setCompanyname(self,cname):
        self.driver.find_element(By.ID,self.txtCompanyName_id).send_keys(cname)
    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdmincomment_xpath).send_keys(content)
    def clickOnSave(self):
        self.driver.find_element(By.NAME,self.btnSave_name).click()
    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdbtnMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdbtnFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdbtnFemaleGender_id).click()

    def setManagerofVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpManagerofVendor_xpath))
        drp.select_by_visible_text(value)

    def setCustomerRoles(self, role):
        #self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]/span").click()
        self.driver.find_element(By.XPATH, self.txtCustomerroles_xpath).click()
        self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
        self.driver.find_element(By.XPATH, self.txtCustomerroles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # User can only be a guest or registered but not both
           # self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Vendors':
            self.listitem= self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        elif role == 'Forum Moderators':
            self.listitem= self.driver.find_element(By.XPATH, self.lstitemForummoderators_xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)



