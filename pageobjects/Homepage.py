from selenium.webdriver.common.by import By

class Homepage:
    myaccount_xpath = "//span[normalize-space()='My Account']"
    register_xpath = "//a[normalize-space()='Register']"
    login_xpath = "//a[normalize-space()='Login']"


    def __init__(self,driver):
        self.driver=driver


    def clickmyaccount(self):
        self.driver.find_element(By.XPATH,self.myaccount_xpath).click()

    def click_register(self):
        self.driver.find_element(By.XPATH,self.register_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()