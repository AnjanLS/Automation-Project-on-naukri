import pytest
import requests
from utilities.BaseClass import BaseClass


class Test_pagestatus(BaseClass):

    url = "https://www.naukri.com/"

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self):
        outcome = yield
        report = outcome.get_result()
        print(report)

    def test_page_responding(self):
        log = self.getLogger()
        response = requests.get(self.url)
        assert response.status_code == 200, log.info(f"Page {self.url} is not responding successfully")
