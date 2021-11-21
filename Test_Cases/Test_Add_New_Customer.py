from Test_Cases.random import random_generator
from Utilities.ReadConfig import ReadConfig
from PageObjectModel.Addcustomerpage import AddCustomer
from PageObjectModel.LoginPage import loginpage
import pytest
import string
import random
class Test_Addcustomer_001:
    url = ReadConfig.url()
    username = ReadConfig.username()
    password = ReadConfig.password()




    def test_new_customer(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.login=loginpage(self.driver)
        self.login.setemail(self.username)
        self.login.setpassword(self.password)
        self.login.clicklogin()

        self.new_customer=AddCustomer(self.driver)
        self.new_customer.clickoncustomer_main_menu()
        self.new_customer.clickoncustomer_menu_item()
        self.new_customer.clickonAdd()

        self.email=random_generator()+"@gmail.com"
        self.new_customer.setcustomer_email(self.email)
        self.new_customer.setcustomer_password("765530976")
        self.new_customer.setcustomer_First_name("Wasim")
        self.new_customer.setcustomer_Last_name("Akram")
        self.new_customer.set_gender('Male')
        self.new_customer.setcustomer_dob("7/05/1985")
        self.new_customer.setcustomer_company_name("Cisco")
        #self.new_customer.customer_tax_exempt()
        #self.new_customer.addcomment("New to this website")
        self.new_customer.Customer_roles("Guests")
        self.new_customer.manage_vendor("Vendor 1")
        self.new_customer.clickonsave()

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_addCustomer_scr.png")  # Screenshot

            assert False

        self.driver.close()

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return "".join(random.choice(chars) for x in range(size))





