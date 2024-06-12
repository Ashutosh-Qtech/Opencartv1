import time

import pytest
from selenium.webdriver.common.by import By

from pageobjects.HRKonnect_logout_screen import Logout_screen
from pageobjects.Loginpage_hrkonnect import Loginpage_hrkonnect

from utilities import excel_utility

from utilities.readproperties import Readconfig

class Test_login_DDT:

    baseurl=Readconfig.getappurl()

    path="G:\\My Drive\\QA Automation\\OpencartV1\\testdata\\HRkonnect login test data.xlsx"


    def test_login_ddt(self,setup):

        self.rows=excel_utility.GetRowCount(self.path,"sheet1")

        list_status=[]

        self.driver=setup

        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.hrkonnect_login_object=Loginpage_hrkonnect(self.driver)
        self.hrkonnect_logout_object=Logout_screen(self.driver)

        for r in range(2,6):

            self.email=excel_utility.GetReaddata(self.path,"sheet1",r,1)
            self.password=excel_utility.GetReaddata(self.path,"sheet1",r,2)
            self.exp=excel_utility.GetReaddata(self.path,"sheet1",r,3)
            self.hrkonnect_login_object.setusername(self.email)
            time.sleep(1)
            self.hrkonnect_login_object.setpwd(self.password)
            time.sleep(1)
            self.hrkonnect_login_object.clicklogin()

            time.sleep(2)

            if self.driver.title=="My Attendance":

                self.hrkonnect_logout_object.cliklogout()

            else:
                self.driver.find_element(By.XPATH,Loginpage_hrkonnect.username_relxpath).clear()
                self.driver.find_element(By.XPATH, Loginpage_hrkonnect.Password_relxpath).clear()



        self.driver.close()




