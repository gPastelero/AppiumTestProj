import unittest
import os
import sys

#command to call test suite:
#py.test -v -s .\AppiumFramework\tests\TestSuite.py --alluredir='AppiumFramework/reports/allurereports'
#command to open allure reports:
#allure serve AppiumFramework\reports\allurereports
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
from AppiumFramework.tests.LoginTest import LoginTest
from AppiumFramework.tests.ContactUsFormTest import ContactFormTest

#create object of the class using unitTest
#cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
#lt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

#create test suite
#regressionTest = unittest.TestSuite([cf,lt])
#regressionTest = unittest.TestSuite([cf,lt])

#call test runner method
#unittest.TextTestRunner(verbosity=1).run(regressionTest)