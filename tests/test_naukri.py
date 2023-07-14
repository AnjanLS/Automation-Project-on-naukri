import pytest
from TestData.LogInData import LogInData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestJob_search(BaseClass):

    def test_naukri(self, getData):
        log = self.getLogger()
        log_in_page = LoginPage(self.driver)
        log_in_page.LogIn()
        log.info("Entering login details")
        log_in_page.Email(getData["email"])
        log_in_page.Password(getData["password"])
        homepage = log_in_page.Submit()
        log.info("Entering job searching details")
        homepage.SearchBar()
        homepage.Designation()
        homepage.Exp()
        homepage.Exp_Yrs()
        homepage.Loc()
        resultpage = homepage.Search()
        log.info("making filter-out the details")
        resultpage.WFO()
        resultpage.Hybrid()
        resultpage.WFH()
        resultpage.Remote()
        resultpage.Department()
        resultpage.Domain_1()
        resultpage.Domain_2()
        resultpage.Apply()
        self.driver.execute_script("window.scrollTo(0, 600)")
        resultpage.Sal_1()
        resultpage.Sal_2()
        self.driver.execute_script("window.scrollTo(0, 900)")
        resultpage.Role_1()
        resultpage.Role_2()
        resultpage.Education()
        resultpage.Posted_By()
        resultpage.Loc()
        log.info("fetched all the details according to employee need!")
        self.Scrolling()
        resultpage.Profile()
        resultpage.LogOut()
        self.driver.get("https://www.naukri.com/")


@pytest.fixture(params=LogInData.getTestData("Testcase3"))
def getData(request):
    return request.param