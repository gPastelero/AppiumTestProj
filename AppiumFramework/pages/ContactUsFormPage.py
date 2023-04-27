import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utils.CustomLogger as cl

class ContactForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #Locator vals in page
    _contactFormButton='com.code2lead.kwad:id/ContactUs' #id
    _pageTitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "4"  # index number
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self._contactFormButton,'id')
        cl.allureLogs('Clicked on Contact us Form Button')
    
    def verifyContactPage(self):
        assert self.isDisplayed(self._pageTitle,'text') == True
        cl.allureLogs("Contact Us Form page opened")

    def enterName(self):
        self.sendText("bob",self._enterName,"text")
        cl.allureLogs("Entered Name")

    def enterEmail(self):
        self.sendText("bob@bobmail.bob",self._enterEmail,"text")
        cl.allureLogs("Entered Email")

    def enterAddress(self):
        self.sendText("USA",self._enterAddress,"text")
        cl.allureLogs("Entered Address")

    def enterNumber(self):
        self.sendText("808",self._enterMobileNumber,"index")
        cl.allureLogs("Entered Mobile Number")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton,"text")
        cl.allureLogs("Clicked on Submit button")