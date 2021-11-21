

class loginpage:
    email_textbox_id="Email"
    password_textbox_id="Password"
    clicklogin_xpath="//button[@type='submit']"
    clicklogout_xpath="//a[contains(text(),'Logout')]"




    def __init__(self,driver):
        self.driver=driver


    def setemail(self,email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.clicklogin_xpath).click()

    def clicklogout(self):
       self.driver.find_element_by_xpath(self.clicklogout_xpath).click()