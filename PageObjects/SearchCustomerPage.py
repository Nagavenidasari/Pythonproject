import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class SearchCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#' ]//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    txt_email_id="SearchEmail"
    txt_firstname_id="SearchFirstName"
    txt_lastname_id="SearchLastName"
    btn_search_id="search-customers"
    tblSearchResults_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    table_rows_xpath="//table[@id='customers-grid']/tbody/tr"
    table_cols_xpath="//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setFirstname(self,fname):
        self.driver.find_element(By.ID,self.txt_firstname_id).clear()
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.ID,self.txt_lastname_id).clear()
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.btn_search_id).click()

    def getRowscount(self):
        print("Number of Rows:", len(self.driver.find_elements(By.XPATH,self.table_rows_xpath)))
        return len(self.driver.find_elements(By.XPATH,self.table_rows_xpath))

    def getColscount(self):
        return len(self.driver.find_elements(By.XPATH,self.table_cols_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getRowscount()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            print("Email Id in the table: ", emailid)
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,name):
        print("Name sent: ",name)
        flag = False
        for r in range(1,self.getRowscount()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            Name_tab=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            print("Name in the table: ", Name_tab)
            if Name_tab == name:
                flag = True
                break
            else:
                flag = False
        return flag


