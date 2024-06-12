import time

import pytest

from pageobjects.Loginpage_hrkonnect import Loginpage_hrkonnect

from utilities.readproperties import Readconfig


class Test_login:
    baseURL = Readconfig.getappurl()
    username = Readconfig.getuseremail()
    Password = Readconfig.getpassword()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.loginpage_object = Loginpage_hrkonnect(self.driver)
        self.loginpage_object.setusername(self.username)
        self.loginpage_object.setpwd(self.Password)
        time.sleep(2)
        self.loginpage_object.clicklogin()

        self.driver.close()
