import os
import sys
import unittest
import pytest
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
#print('===================================')
from AppiumFramework.base.DriverClass import Driver
import AppiumFramework.utils.CustomLogger as cl
from AppiumFramework.pages.LoginPage import LoginPage
from AppiumFramework.base.BasePage import BasePage
#print(sys.path[0])

@pytest.mark.usefixtures('beforeClass','beforeMethod')
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lt = LoginPage(self.driver)
        self.bp= BasePage(self.driver)
        
    
    @pytest.mark.run(order=4)
    def test_openLoginScreen(self):
        self.bp.keyCode(4) #press back
        self.lt.clickLoginButton()
        self.lt.enterEmail()
        self.lt.enterPassword()
        self.lt.clickOnLoginB()
        self.lt.verifyAdminScreen()
    
    @pytest.mark.run(order=3)
    def test_loginFail(self):
        cl.allureLogs('App opened')
        self.lt.clickLoginButton()
        self.lt.enterEmail()
        self.lt.enterPassword2()
        self.lt.clickOnLoginB()
        self.lt.verifyAdminScreen()
    
    @pytest.mark.run(order=5)
    def test_enterAdmin(self):
        self.lt.enterText()
        self.lt.clickOnSubmit()

