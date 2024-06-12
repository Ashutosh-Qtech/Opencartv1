import time

from pageobjects.Homepage import Homepage
from pageobjects.Accountregistrationpage import Account_registration_page
from utilities import randomstring
from utilities.readproperties import Readconfig
from utilities.customlogger import Loggen


class Test_01_accountereg:
    base_url = Readconfig.getappurl()
    logger=Loggen.loggen()

    def test_account_reg(self,setup):

        # self.logger.info("test_0010_account registration started")




        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)

        self.driver.maximize_window()



        self.hp=Homepage(self.driver)
        self.hp.clickmyaccount()
        self.hp.click_register()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


        self.regpage=Account_registration_page(self.driver)
        self.regpage.setfname("Ashutosh")
        self.regpage.setlname("verma")
        time.sleep(3)
        self.email=randomstring.random_string_generator()+'@gmail.com'
        self.regpage.setemail(self.email)
        self.regpage.setpass("abcxyz")

        self.regpage.policy_checkmark()
        time.sleep(2)
        self.regpage.Continue_Button_click()
        self.driver.close()



