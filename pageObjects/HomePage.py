import time
from selenium.webdriver.common.by import By
from pageObjects.ResultPage import ResultPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_bar = (By.XPATH, "//span[@class='nI-gNb-sb__placeholder']")
    designation = (By.XPATH, "(//input[@class='suggestor-input '])[1]")
    exp = (By.XPATH, "//div/div/div/input[@id='experienceDD']")
    exp_years = (By.XPATH, "//div/ul/li/div/span[text()='2 years']")
    loc = (By.XPATH, "//div/div/div/div/input[@placeholder='Enter location']")
    search = (By.XPATH, "//button")

    def SearchBar(self):
        self.driver.find_element(*HomePage.search_bar).click()

    def Designation(self):
        self.driver.find_element(*HomePage.designation).send_keys("Software Engineer")

    def Exp(self):
        self.driver.find_element(*HomePage.exp).click()

    def Exp_Yrs(self):
        self.driver.find_element(*HomePage.exp_years).click()

    def Loc(self):
        self.driver.find_element(*HomePage.loc).send_keys("Bangalore")
        time.sleep(3)

    def Search(self):
        self.driver.find_element(*HomePage.search).click()
        resultpage = ResultPage(self.driver)
        return resultpage