import time
from selenium.webdriver.support.ui import Select

class AddCustomer:

    Customer_main_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    Customer_sub_menu_xpath="//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    add_xpath="//a[@class='btn btn-primary']"
    customer_email_xpath="//input[@id='Email']"
    pasword_xpath="//input[@id='Password']"
    First_name_xpath="//input[@id='FirstName']"
    Last_name_xpath="//input[@id='LastName']"
    customer_gender_male_xpath="//input[@id='Gender_Male']"
    customer_gender_female_xpath="//input[@id='Gender_Female']"
    customer_dob_xpath="//input[@id='DateOfBirth']"
    customer_company_xpath="//input[@id='Company']"
    customer_tax_exempt="//input[@id='IsTaxExempt']"

    customer_roles_main_xpath="//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    customer_role_as_registered_xpath='//li[contains(text(),"Registered")]'
    customer_role_as_guest_xpath='//li[contains(text(),"Guests")]'
    customer_role_as_vendor_xpath='//li[contains(text(),"Vendors")]'
    customer_role_as_administartor_xpath='//li[contains(text(),"Administrators")]'
    manager_of_vendor_xpath='//select [@id="VendorId"]'
    add_comment_xpath='//textarea [@id="AdminComment"]'
    save_button_xpath='//button [@name="save"]'

    def __init__(self,driver):
        self.driver=driver


    def clickoncustomer_main_menu(self):
        self.driver.find_element_by_xpath(self.Customer_main_menu_xpath).click()

    def clickoncustomer_menu_item(self):
        self.driver.find_element_by_xpath(self.Customer_sub_menu_xpath).click()
    def clickonAdd(self):
        self.driver.find_element_by_xpath(self. add_xpath).click()


    def setcustomer_email(self,email):
        self.driver.find_element_by_xpath(self.customer_email_xpath).clear()
        self.driver.find_element_by_xpath(self.customer_email_xpath).send_keys(email)

    def setcustomer_password(self,password):
        self.driver.find_element_by_xpath(self.pasword_xpath).clear()
        self.driver.find_element_by_xpath(self.pasword_xpath).send_keys(password)

    def setcustomer_First_name(self,first_name):
        self.driver.find_element_by_xpath(self.First_name_xpath).clear()
        self.driver.find_element_by_xpath(self.First_name_xpath).send_keys(first_name)

    def setcustomer_Last_name(self,last_name):
        self.driver.find_element_by_xpath(self.Last_name_xpath).clear()
        self.driver.find_element_by_xpath(self.Last_name_xpath).send_keys(last_name)

    def setcustomer_dob(self,dob):
        self.driver.find_element_by_xpath(self.customer_dob_xpath).clear()
        self.driver.find_element_by_xpath(self.customer_dob_xpath).send_keys(dob)
    def setcustomer_company_name(self,company_name):
        self.driver.find_element_by_xpath(self.customer_company_xpath).clear()
        self.driver.find_element_by_xpath(self.customer_company_xpath).send_keys(company_name)

    def select_tax_exempt(self):
        self.driver.find_element_by_xpath(self.customer_tax_exempt).click()
    def addcomment(self,comment):
        self.driver.find_element_by_xpath(self. add_comment_xpath).clear()
        self.driver.find_element_by_xpath(self. add_comment_xpath).send_keys(comment)
    def manage_vendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.manager_of_vendor_xpath))
        drp.select_by_visible_text(value)

    def Customer_roles(self,roles):
        self.driver.find_element_by_xpath(self.customer_roles_main_xpath).click()
        time.sleep(2)

        if roles=="Registered":
            self.listitem=self.driver.find_element_by_xpath(self.customer_role_as_registered_xpath)
        elif roles=="Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.customer_role_as_vendor_xpath)
        elif roles=="Administrators":
            self.listitem=self.driver.find_element_by_xpath(self.customer_role_as_administartor_xpath)
        elif roles=="Guests":
            self.driver.find_element_by_xpath(self.customer_role_as_registered_xpath).click()
            self.listitem=self.driver.find_element_by_xpath(self.customer_role_as_guest_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.customer_role_as_guest_xpath)

        time.sleep(3)
        #click on listitem
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def set_gender(self,value):

        if value=="Male":
            self.driver.find_element_by_xpath(self.customer_gender_male_xpath).click()
        elif value == "Female":
            self.driver.find_element_by_xpath(self.  customer_gender_female_xpath).click()

        else:
            self.driver.find_element_by_xpath(self.customer_gender_male_xpath).click()


    def clickonsave(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
