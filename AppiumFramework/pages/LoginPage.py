import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utils.CustomLogger as cl

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
    
    #Locators
    _loginButton='com.code2lead.kwad:id/Login'
    _email='com.code2lead.kwad:id/Et4'
    _password='com.code2lead.kwad:id/Et5'
    _submit='com.code2lead.kwad:id/Btn3'
    _adminTextBox='com.code2lead.kwad:id/Edt_admin'
    _adminSubmit='com.code2lead.kwad:id/Btn_admin_sub'
    _adminTitle='Enter Admin'

    def clickLoginButton(self):
        self.clickElement(self._loginButton,"id")
        cl.allureLogs("Click on Login Button")

    def enterEmail(self):
        self.sendText("admin@gmail.com",self._email,"id")
        cl.allureLogs("Entered email id")

    def enterPassword(self):
        self.sendText("admin123",self._password,"id")
        cl.allureLogs("Entered Password")

    def enterPassword2(self):
        self.sendText("wrongPass",self._password,"id")
        cl.allureLogs("Entered Wrong Password")

    def clickOnLoginB(self):
        self.clickElement(self._submit,"id")
        cl.allureLogs("Clicked on Login Button in Login Screen")

    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self._adminTitle,"text")
        assert adminScreen == True
        cl.allureLogs("Opened Admin Screen")

    def enterText(self):
        self.sendText("adminBob",self._adminTextBox,"id")
        cl.allureLogs("Entered Text")

    def clickOnSubmit(self):
        self.clickElement(self._adminSubmit,"id")
        cl.allureLogs("Clicked on Submit Button")
