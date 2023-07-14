import time
from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    wfo = (By.XPATH, "(//div/label/i[@class='fleft naukicon naukicon-checkbox'])[1]")
    hybrid = (By.XPATH, "//div/label/p/span[@title='Hybrid']")
    wfh = (By.XPATH, "//div/label/p/span[@title='Temp. WFH due to covid']")
    remote = (By.XPATH, "//div/label/p/span[@title='Remote']")
    department = (By.XPATH, "(//a/span[@class='fleft'])[1]")
    domain_1 = (By.XPATH, "(//span[@title='Engineering - Software & QA'])[2]")
    domain_2 = (By.XPATH, "//span[@title='Quality Assurance']")
    apply = (By.XPATH, "//div[@class='filter-apply-btn ']")
    sal_1 = (By.XPATH, "//span[@title='3-6 Lakhs']")
    sal_2 = (By.XPATH, "//span[@title='6-10 Lakhs']")
    role_1 = (By.XPATH, "//span[@title='Software Development']")
    role_2 = (By.XPATH, "//span[@title='Quality Assurance and Testing']")
    education = (By.XPATH, "//span[@title='Any Graduate']")
    posted_by = (By.XPATH, "//span[@title='Company Jobs']")
    loc = (By.XPATH, "//span[@title='Bangalore/Bengaluru']")
    profile = (By.XPATH, "//img[@alt='naukri user profile img']")
    logout = (By.XPATH, "//a[normalize-space()='Logout']")

    def WFO(self):
        self.driver.find_element(*ResultPage.wfo).click()

    def Hybrid(self):
        self.driver.find_element(*ResultPage.hybrid).click()

    def WFH(self):
        self.driver.find_element(*ResultPage.wfh).click()

    def Remote(self):
        self.driver.find_element(*ResultPage.remote).click()

    def Department(self):
        self.driver.find_element(*ResultPage.department).click()

    def Domain_1(self):
        self.driver.find_element(*ResultPage.domain_1).click()

    def Domain_2(self):
        self.driver.find_element(*ResultPage.domain_2).click()

    def Apply(self):
        self.driver.find_element(*ResultPage.apply).click()

    def Sal_1(self):
        self.driver.find_element(*ResultPage.sal_1).click()

    def Sal_2(self):
        self.driver.find_element(*ResultPage.sal_2).click()
        time.sleep(5)

    def Role_1(self):
        self.driver.find_element(*ResultPage.role_1).click()

    def Role_2(self):
        self.driver.find_element(*ResultPage.role_2).click()

    def Education(self):
        self.driver.find_element(*ResultPage.education).click()

    def Posted_By(self):
        self.driver.find_element(*ResultPage.posted_by).click()

    def Loc(self):
        self.driver.find_element(*ResultPage.loc).click()
        time.sleep(10)

    def Profile(self):
        self.driver.find_element(*ResultPage.profile).click()

    def LogOut(self):
        self.driver.find_element(*ResultPage.logout).click()





