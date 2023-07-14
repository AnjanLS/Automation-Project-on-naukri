import inspect
import logging
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseClass:

    def Scrolling(self):
        num_iterations = 10  # number of scrolls
        body = self.driver.find_element(By.TAG_NAME, "body")
        for i in range(num_iterations):
            body.send_keys(Keys.PAGE_DOWN)  # To scroll down
            time.sleep(3)  # wait for each iteration
        self.driver.execute_script("window.scrollTo(0, 0);")  # To scroll up
        time.sleep(5)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger