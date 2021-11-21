from Utilities.ReadConfig import ReadConfig
from PageObjectModel.LoginPage import loginpage
from Utilities.logs import logger


class Test_case_logintest:
    url=ReadConfig.url()
    username=ReadConfig.username()
    password=ReadConfig.password()
    logger=logger.loggen()
    @pytest.mark.sanity
    def test_login(self,setup):
        print(self.logger.info("************Test started********************"))
        self.driver=setup
        self.driver.get(self.url)
        print(self.driver.title)

        lp=loginpage(self.driver)
        lp.setemail(self.username)
        lp.setpassword(self.password)
        lp.clicklogin()
        print(self.driver.title)
        lp.clicklogout()
        self.driver.close()










