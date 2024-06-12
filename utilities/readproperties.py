import  configparser
import os

config=configparser.RawConfigParser()

config.read("G:\My Drive\QA Automation\OpencartV1\configuration\config.ini")



class Readconfig:

    @staticmethod
    def getappurl():
        url=config.get('commonInfo','baseURL')
        return url



    @staticmethod
    def getuseremail():
        useremail=config.get('commonInfo','email')
        return useremail


    @staticmethod
    def getpassword():
        password=config.get('commonInfo','password')
        return password

