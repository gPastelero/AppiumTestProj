import inspect
import logging
import os
import allure

def customLogger():
    #get file/method name that this is being called from
    logName = inspect.stack()[1][3]
    print('LOG NAME: '+logName)

    #create logging obj and pass logName into it
    logger=logging.getLogger(logName)

    #Set log level
    logger.setLevel(logging.DEBUG)

    #create fileHandler
    fh = logging.FileHandler(os.path.dirname(os.path.realpath(__file__))+"/../reports/code2lead.log".format(logName),mode='a')

    #set logLevel for fileHandler
    fh.setLevel(logging.DEBUG)

    #create format for logging
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %t %I:%M:%S %p %A',)
    
    #set formatter to filehandler
    fh.setFormatter(formatter)

    #add fh to logger
    logger.addHandler(fh)

    #return logging object
    return logger

def allureLogs(text):
    with allure.step(text): #writes text to logs in allure report
        pass
