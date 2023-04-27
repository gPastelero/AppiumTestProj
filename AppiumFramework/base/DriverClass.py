import os
import time
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
import AppiumFramework.utils.CustomLogger as cl
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException

class Driver:
    def getDriver(self):
        #get path of demo apk
        apkPath = os.path.dirname(os.path.realpath(__file__))+"/../../resources/Android_Demo_App.apk"

        #start appium server
        global appiumService 
        appiumService= AppiumService()
        appiumService.start(args=["--base-path", "/wd/hub"])

        #initialize desired capabilities
        desired_caps = {} 
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName']= 'UiAutomator2'
        desired_caps['platformVersion'] = '13' 
        desired_caps['deviceName'] = 'Pixel 3a XL' 
        desired_caps['app'] = (apkPath) 
        desired_caps['appPackage'] = 'com.code2lead.kwad' 
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity' 

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=
                    [ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
        
        return driver

    def exit(self, driver):
        time.sleep(4)
        log = cl.customLogger()
        driver.quit()
        appiumService.stop()
        log.info('App successfully closed')
    
    def test(self):
        print('here')

#test = Driver()
#test.exit(test.getDriver())