from selenium.webdriver.common.by import By

class Account_registration_page:
    first_name="//input[@id='input-firstname']"
    last_name="//input[@id='input-lastname']"
    email_xpath="//input[@id='input-email']"
    password="//input[@id='input-password']"
    policy_check_mark_xpath="//input[@name='agree']"
    button_continue="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def setfname(self,fname):
        self.driver.find_element(By.XPATH,self.first_name).send_keys(fname)

    def setlname(self, lname):
        self.driver.find_element(By.XPATH, self.last_name).send_keys(lname)

    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def setpass(self,pwd):
        self.driver.find_element(By.XPATH, self.password).send_keys(pwd)

    def policy_checkmark(self):

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.policy_check_mark_xpath).click()


    def Continue_Button_click(self):
        self.driver.find_element(By.XPATH, self.button_continue).click()
