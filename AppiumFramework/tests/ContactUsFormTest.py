import os
import sys
import unittest
import pytest
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
#print('===================================')
from AppiumFramework.base.DriverClass import Driver
import AppiumFramework.utils.CustomLogger as cl
from AppiumFramework.pages.ContactUsFormPage import ContactForm
#print(sys.path[0])

@pytest.mark.usefixtures('beforeClass','beforeMethod')
class ContactFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)
        #log= cl.customLogger()
    
    @pytest.mark.run(order=1)
    def test_openContactForm(self):
        cl.allureLogs('App launched')
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
    
    @pytest.mark.run(order=2)
    def test_enterData(self):
        cl.allureLogs('Entering data')
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterNumber()
        self.cf.enterAddress()
        self.cf.clickSubmitButton()




