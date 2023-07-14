import time
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login = (By.XPATH, "//div/a[@id='login_Layer']")
    email = (By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")
    password = (By.XPATH, "//input[@type='password']")
    submit = (By.XPATH, "//button[@type='submit']")

    def LogIn(self):
        self.driver.find_element(*LoginPage.login).click()

    def Email(self, email):
        self.driver.find_element(*LoginPage.email).send_keys(email)

    def Password(self, password):
        self.driver.find_element(*LoginPage.password).send_keys(password)

    def Submit(self):
        self.driver.find_element(*LoginPage.submit).click()
        time.sleep(3)
        homepage = HomePage(self.driver)
        return homepage