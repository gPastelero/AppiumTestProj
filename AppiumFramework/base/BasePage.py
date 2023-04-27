import os
import sys
import time
import allure
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from appium.webdriver.common.appiumby import AppiumBy
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
import AppiumFramework.utils.CustomLogger as cl

class BasePage:
    log = cl.customLogger()
    def __init__(self,driver):
        self.driver=driver
    
    def waitForEle(self,locatorvalue,locatorType):
        locatorType=locatorType.lower()
        wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=
                [ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
        
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID,locatorvalue))
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME,locatorvalue))
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("%s")' % (locatorvalue)))
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(%d)" % int(locatorvalue)))
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("%s")' % locatorvalue))
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH,'%s' % (locatorvalue)))
        else:
            self.log.info("Locator value " + locatorvalue + "not found")
 
        return element
        
    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForEle(locatorValue, locatorType)
            self.log.info(
                "Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
           
        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
    
    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
            return True
        except:
            self.log.info(
                "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            self.takeScreenshot(locatorType)
            return False
        
    
    def screenShot(self, ssName):
        fileName= ssName+'_'+(time.strftime('%d_%m_%y_%H_%M_%S'))+'.png'
        dir = 'screenshots/'
        path = dir+fileName

        try:
            self.driver.save_screenshot(path)
            self.log.info('Screenshot saved to path: '+path)
        
        except:
             self.log.info('Screenshot unable to save to path: '+path)
    
    def takeScreenshot(self,text):
        allure.attach(self.driver.get_screenshot_as_png(),name=text, attachment_type=allure.attachment_type.PNG)

    def keyCode(self,value):
        self.driver.press_keycode(value)