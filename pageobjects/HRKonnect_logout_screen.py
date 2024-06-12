from  selenium.webdriver.common.by import By

class Logout_screen:

    logout_xpath="//a[@id='ctl00_ctl00_LogOut_lnklogout']"

    def __init__(self,driver):
        self.driver=driver

    def cliklogout(self):

        self.driver.find_element(By.XPATH,self.logout_xpath).click()


