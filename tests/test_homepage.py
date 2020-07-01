import pytest

from PageObjects.HomePage import HomePage
from Utility.BaseClass import BaseClass


class TestHomepage(BaseClass):

    def test_homepage(self, get_multiple_data):
        homepage = HomePage(self.driver)
        self.driver.refresh()
        homepage.enter_name().send_keys(get_multiple_data[0])
        homepage.enter_email().send_keys(get_multiple_data[1])
        self.select_text(homepage.enter_gender(), get_multiple_data[2])
        homepage.submit_button().click()
        assert "Success!" in homepage.get_success().text



