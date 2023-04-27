#constant file name
#applies to all files being tested
import os
import time
import pytest
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
#import AppiumFramework.utils.CustomLogger as cl
#log= cl.customLogger()
#log.info('CURRENT PATH: '+sys.path[0])

from AppiumFramework.base.DriverClass import Driver
'''
Notes for rerunning tests
pytest --reruns [x] #x is number of times to rerun failed tests
pytest --reruns [x] --reruns-delay [y] #y is the number of seconds to wait between reruns
py.test -v -s .\AppiumFramework\tests\LoginTest.py --alluredir='AppiumFramework/reports/allurereports'
'''

#Before/after class
@pytest.fixture(scope='class') #decorator
def beforeClass(request):
    #Before
    print('\n========================')
    print('Before a class') 
    driver1 = Driver()
    driver = driver1.getDriver()
    if request.cls is not None:
        request.cls.driver = driver 
    yield driver
    time.sleep(5)
    driver.quit()

    #After
    print('\nAfter class')
    print('========================')


#Before/after method
@pytest.fixture() #decorator
def beforeMethod():
    #Before
    print('\n--------------------')
    print('Before a method') 
    
    yield

    #After
    print('\nAfter method')
    print('--------------------')

