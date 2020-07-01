from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//button[@class='btn btn-success']")
    country = (By.ID, "country")
    country_select = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    conditions = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    success = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def clcik_checkout(self):
        return self.driver.find_element(* ConfirmPage.checkout)

    def enter_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def get_xpath(self):
        return "//div[@class='suggestions']/ul/li/a"

    def select_entered_country(self):
        return self.driver.find_element(*ConfirmPage.country_select)

    def check_conditions(self):
        return self.driver.find_element(*ConfirmPage.conditions)

    def click_purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def get_success(self):
        return self.driver.find_element(*ConfirmPage.success)





