from selenium import webdriver
from selenium.webdriver.common.by import By


class Loginpage_hrkonnect:

    username_relxpath="//input[@id='txtEmpCode']"
    Password_relxpath="//input[@id='txtPswd']"
    login_button="//input[@id='btnSubmit']"


##below is the constructor which will initiates the driver

    def __init__(self,driver):
        self.driver=driver


## below are the action methods


    def setusername(self,username):
        self.driver.find_element(By.XPATH,self.username_relxpath).send_keys(username)

    def setpwd(self,pwd):
        self.driver.find_element(By.XPATH,self.Password_relxpath).send_keys(pwd)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.login_button).click()

