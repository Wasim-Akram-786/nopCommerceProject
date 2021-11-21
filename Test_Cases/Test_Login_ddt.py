import time

import pytest

from Utilities.ReadConfig import ReadConfig
from PageObjectModel.LoginPage import loginpage
from Utilities.logs import logger
from Utilities import XLutils

class Test_case_logintest:
    url=ReadConfig.url()
    username=ReadConfig.username()
    password=ReadConfig.password()
    logger=logger.loggen()
    file='.//Test-Data//LoginData.xlsx'

   
    def test_login_ddt(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.lp=loginpage(self.driver)
        #read no of rows in sheet
        self.row=XLutils.getrowcount(self.file,'Sheet1')
        print(self.row)

        for r in range(2,self.row+1):
            self.user=XLutils.readdata(self.file,'Sheet1',r,1)
            self.password=XLutils.readdata(self.file,'Sheet1',r,2)
            self.exp=XLutils.readdata(self.file,'Sheet1' ,r,3)

            self.lp.setemail(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)
            lst=[]
            act_title=self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            #Validation
            if act_title==exp_title:
                if self.exp=="Pass":
                    print("Passed")
                    self.lp.clicklogout()
                    lst.append('Pass')
                elif self.exp=='Fail':
                    print('Failed')
                    self.lp.clicklogout()
                    lst.append('Fail')
            elif act_title!=exp_title:
                if self.exp=='Pass':
                    print('Failed')

                    lst.append('Fail')
                elif self.exp=='Fail':
                    print("Pass")

                    lst.append('Pass')
            print(lst)

        if 'Fail' not in lst:
            print("Test Case passed")
            self.driver.close()
            assert True
        else:
            print('Test case Failed')
            self.driver.close()
            assert False




